# Generated by Django 3.2.20 on 2023-07-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_property_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
