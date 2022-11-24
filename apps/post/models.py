from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from .utils import get_time
from slugify import slugify

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, primary_key=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Apartment(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, primary_key=True, blank=True)
    address = models.CharField(max_length=50)
    rooms = models.IntegerField(default=0)
    square_meters = models.IntegerField(default=0)
    description = models.TextField() # описание
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0) # количество просмотров
    category = models.ForeignKey(
        to=Category, 
        on_delete=models.CASCADE,
        related_name='apartments',
        )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='products',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + get_time())
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class CurrentPostDefault:
    requires_context = True
    
    def __call__(self, serializer_field):
        return serializer_field.context['post']



