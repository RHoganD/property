# Generated by Django 3.2.20 on 2023-07-28 17:39

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='agents/')),
            ],
        ),
    ]
