from django.urls import path

from .views import FavoritPostsView



urlpatterns = [
    path('favorited/', FavoritPostsView.as_view(), name='favorited')
]