
from rest_framework.generics import ListAPIView
from .models import Favorites
from .serializers import FavoritesPostSerializer
from rest_framework.permissions import IsAuthenticated



class FavoritPostsView(ListAPIView):
    serializer_class = FavoritesPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Favorites.objects.filter(user=user)