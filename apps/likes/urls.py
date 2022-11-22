from django.urls import path

from .views import LikePostsView



urlpatterns = [
    path('liked/', LikePostsView.as_view(), name='liked')
]