from django.urls import path

from .views import RatingViewSet



urlpatterns = [
    path('rating/', RatingViewSet.as_view(), name='rating')
]