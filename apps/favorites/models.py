from django.db import models
from apps.post.models import Apartment
from django.contrib.auth import get_user_model

User = get_user_model()


class Favorites(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='favorit',
        blank=True,
        null=True
    )
    apartment = models.ForeignKey(
        to=Apartment,
        on_delete=models.CASCADE,
        related_name='favorites',
        blank=True
    )

    def __str__(self) -> str:
        return f'Added to favorites {self.user.username}'


