# Generated by Django 3.2.20 on 2023-07-29 12:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured_img',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='images'),
        ),
    ]