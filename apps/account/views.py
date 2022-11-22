from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    SetRestoredPasswordSerializer,
    UserRegistrationSerializer, 
    PasswordChangeSerializer,
    RestorePasswordSerializer
    )


User = get_user_model()


class RegistrationView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request: Request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Спасибо за регистрацию, активируйте аккаунт, код отправлен на ваш email',
                status=status.HTTP_201_CREATED
            )

class AccountActivationView(APIView):
    def get(self, request, activation_code):
        user = User.objects.filter(activation_code=activation_code).first()
        if not user:
            return Response(
                'Страница не найдена', 
                status=status.HTTP_404_NOT_FOUND
                )
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response(
            'Ваш аккаунт активирован! Вы можете войти',
            status=status.HTTP_200_OK
        )


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Пароль успешно изменен!',
                status=status.HTTP_200_OK
            )


class RestorePasswordView(APIView):
    def post(self, request:Request):
        serializer = RestorePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_code()
            return Response(
                'Код отправлен на ваш email!',
                status=status.HTTP_200_OK
            )



class SetRestoredPasswordView(APIView):
    def post(self, request: Request):
        serializer = SetRestoredPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Пароль успешно восстановлен!',
                status=status.HTTP_200_OK
            )


class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def destroy(self, request: Request):
        username = request.user.username
        User.objects.get(username=username).delete()
        return Response(
            'Аккаунт успешно удален!',
            status=status.HTTP_204_NO_CONTENT
        )