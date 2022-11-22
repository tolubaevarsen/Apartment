from urllib import request
from wsgiref.validate import validator
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .tasks import send_activation_code
from django.core.mail import send_mail
from django.conf import settings


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length=128, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Имя пользователя уже занято, выберите другое'
                )
        return username

    
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.create_activation_code()
        send_activation_code.delay(user.email, user.activation_code)
        return user

    
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, required=True)
    new_password = serializers.CharField(max_length=128, required=True)
    new_password_confirm = serializers.CharField(max_length=128, required=True)
    
    def validate_old_password(self, old_password):
        user = self.context.get('request').user
        if not user.check_password(old_password):
            raise serializers.ValidationError(
                'Неправильный пароль!'
            )
        return old_password

    def validate(self, attrs: dict):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def set_new_password(self):
        user = self.context.get('request').user
        password = self. validated_data.get('new_password')
        user.set_password(password)
        user.save()

class RestorePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Пользователя с таким email не существует!'
            )
        return email

    def send_code(self):
        email = self.validated_data.get(email)
        user = User.objects.get(email=email)
        user.create_activation_code()
        send_mail(
            subject = 'Восстановление пароля',
            message=f'Ваш код для восстановления пароля {user.activation_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list = [email]
        )




class SetRestoredPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)
    code = serializers.CharField(min_length=1, max_length=8, required=True)
    new_password = serializers.CharField(max_length=128, required=True)
    new_password_confirm = serializers.CharField(max_length=128, required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Пользователя с таким email не существует!'
            )
        return email

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError(
                'Неправильный пароль!'
            )
        return code

    def validate(self, attrs: dict):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                'Пароли не совпадают!'
                )
        return attrs
        
    def set_new_password(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        new_password = self. validated_data.get('new_password')
        user.set_password(new_password)
        user.activation_code = ''
        user.save()