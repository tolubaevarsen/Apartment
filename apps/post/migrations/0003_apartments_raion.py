# Generated by Django 3.2.5 on 2022-11-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_apartments_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='raion',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
