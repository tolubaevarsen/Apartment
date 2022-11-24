from unicodedata import name
from django.urls import path
from .views import (RegistrationView,
            AccountActivationView,
            ChangePasswordView,
            RestorePasswordView,
            SetRestorePasswordView,
            DeleteAccountView
            )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activate/<str:activation_code>/', AccountActivationView.as_view(), name='activation'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('restore-password/', RestorePasswordView.as_view(), name='restore-password'),
    path('set-restored-password/', SetRestorePasswordView.as_view(), name='set-restored-password'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete_account')
]

# TODO: протестить весь функционал