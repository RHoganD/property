# Generated by Django 3.2.20 on 2023-07-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_viewing_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewing',
            name='phone',
            field=models.IntegerField(),
        ),
    ]