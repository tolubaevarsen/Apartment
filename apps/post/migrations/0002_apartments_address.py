# Generated by Django 3.2.5 on 2022-11-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]