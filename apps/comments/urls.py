from rest_framework.routers import DefaultRouter
from .views import CommentView

router = DefaultRouter()
router.register('comments', CommentView, 'comment')

urlpatterns = [
    
]

urlpatterns += router.urls