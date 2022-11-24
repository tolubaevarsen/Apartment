from django.db import models
from django.contrib.auth import get_user_model
from apps.post.models import Apartment
User = get_user_model()


class Rating(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING_CHOICES = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5')
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES, 
        blank=True, 
        null=True)
    post = models.ForeignKey(
        to=Apartment,
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    def __str__(self):
        return f'{str(self.rating)}'

