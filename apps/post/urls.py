from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ApartmentViewSet

router = DefaultRouter()
router.register('apartments', ApartmentViewSet, 'apartment')
router.register('categories', CategoryViewSet, 'category')

urlpatterns = [
    # path('', include('apps.review.urls'))
]
urlpatterns += router.urls