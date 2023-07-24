from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
property_type = (
  ('S', "Sale"),
  ('R', "Rent"),
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    property_type = models.CharField(choices=property_type, max_length=10)
    price = models.PositiveIntegerField()
    bedrooms_num = models.PositiveIntegerField()
    bathroom_num = models.PositiveIntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    Parking = (
        ('Private', "Private"),
        ('Permit', "Permit"),
    )
    parking = models.CharField(choices=Parking, max_length=15)

    Garden = (
        ('Share', "Share"),
        ('Private', "Private"),
    )
    garden = models.CharField(choices=Garden, max_length=15)


    def __str__(self):
        return self.name