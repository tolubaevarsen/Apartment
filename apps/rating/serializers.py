from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )
    
    class Meta:
        model = Rating
        fields = 'rating', 'user', 'post'

    def validate(self, attrs):
        user = self.context.get('request').user
        attrs['user'] = user 
        rating = attrs.get('rating')
        if rating not in (1,2,3,4,5):
            raise serializers.ValidationError(
                'Wrong value Rating must be between 1 and 5 '
                )
        return attrs

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating')
        return super().update(instance, validated_data)

