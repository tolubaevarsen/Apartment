from rest_framework import serializers
from apps.post.models import CurrentPostDefault

from .models import Like 



class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.HiddenField(default=CurrentPostDefault())
    class Meta:
        model = Like
        fields = '__all__'
    
    def create(self, validated_data):
        user = self.context.get('request').user
        post = self.context.get('post').pk
        like = Like.objects.filter(user=user, post=post).first()
        if like:
            raise serializers.ValidationError('Already liked')
        return super().create(validated_data)
    
    def unlike(self):
        user = self.context.get('request').user
        post = self.context.get('post').pk
        like = Like.objects.filter(user=user, post=post).first()
        if like:
            like.delete()
        else:
            raise serializers.ValidationError('Not liked yet')


class LikedPostSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='post.get_absolute_url')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Like
        fields = ['post', 'user', 'url']
