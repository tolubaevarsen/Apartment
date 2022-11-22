from rest_framework import serializers
from .models import Apartment, Category# ApartmentImage

# from apps.review.serializers import CommentSerializer


class ApartmentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Apartment
        fields = '__all__'

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Цена не может быть отрицательной')
        return price
    
    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
    #     rep['comments_count'] = instance.comments.all().count()
    #     return rep


class ApartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('image', 'title', 'price', 'in_stock', 'slug', 'address', 'description')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments_count'] = instance.comments.all().count()
        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
