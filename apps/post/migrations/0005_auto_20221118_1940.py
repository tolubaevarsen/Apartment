# Generated by Django 3.2.5 on 2022-11-18 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_apartments_raion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=220, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('in_stock', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='product_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='post.category', verbose_name='родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.DeleteModel(
            name='Apartments',
        ),
        migrations.AddField(
            model_name='apartment',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='post.category'),
        ),
    ]