from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from .serializers import (
    CategorySerializer,
    ApartmentSerializer,
    ApartmentListSerializer,
    CategorySerializer
)
from .models import (
    Apartment,
    Category
    )  # ProductImage


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ApartmentListSerializer #product/13
        return ApartmentSerializer # product/

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def retrive(self, request, *args, **kwargs):
        instanse: Apartment = self.get_object()
        instanse.views_count +=1
        instanse .save()
        return super().retrieve(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

