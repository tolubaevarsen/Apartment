# Generated by Django 3.2.5 on 2022-11-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_apartment_square'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='e',
            field=models.CharField(max_length=15, null=True),
        ),
    ]