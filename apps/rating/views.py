from django.shortcuts import render
from .models import Rating
from apps.post.models import Apartment
from apps.post.serializers import ApartmentSerializer
from rest_framework.viewsets import ModelViewSet


class RatingViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    class Meta:
        model = Rating
        fields = ('__all__')

