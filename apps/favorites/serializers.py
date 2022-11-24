from rest_framework import serializers
from apps.post.models import CurrentPostDefault

from .models import Favorites



class FavoritesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.HiddenField(default=CurrentPostDefault())
    class Meta:
        model = Favorites
        fields = '__all__'
    
    def create(self, validated_data):
        user = self.context.get('request').user
        post = self.context.get('post').pk
        favorite = Favorites.objects.filter(user=user, post=post).first()
        if favorite:
            raise serializers.ValidationError('Already in favorites')
        return super().create(validated_data)
    
    def unlike(self):
        user = self.context.get('request').user
        post = self.context.get('post').pk
        favorite = Favorites.objects.filter(user=user, post=post).first()
        if favorite:
            favorite.delete()
        else:
            raise serializers.ValidationError('Not favorites yet')


class FavoritesPostSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='post.get_absolute_url')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Favorites
        fields = ['post', 'user', 'url']
