
from rest_framework.generics import ListAPIView
from .models import Like
from .serializers import LikedPostSerializer
from rest_framework.permissions import IsAuthenticated



class LikePostsView(ListAPIView):
    serializer_class = LikedPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Like.objects.filter(user=user)