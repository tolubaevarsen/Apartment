from django.db import models
from apps.post.models import Apartment
from django.contrib.auth import get_user_model

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='likes',
        blank=True,
        null=True
    )
    apartment = models.ForeignKey(
        to=Apartment,
        on_delete=models.CASCADE,
        related_name='likes',
        blank=True
    )

    def __str__(self) -> str:
        return f'Liked by {self.user.username}'


