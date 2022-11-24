# Generated by Django 3.2.5 on 2022-11-24 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='post.apartment')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
