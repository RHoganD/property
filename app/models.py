from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField



property_type = (
  ('Sale', "Sale"),
  ('Rent', "Rent"),
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    direction = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
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

    Furnished = (
        ('Furnished', "Furnished"),
        ('Unfurnished', "Unfurnished"), 
       
    )
    furniture = models.CharField(choices=Furnished, max_length=15)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    featured_img = CloudinaryField('images', default='placeholder')

    def __str__(self):
        return  self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Viewing(models.Model):
    customer_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField(max_length=100)
 

    def __str__(self):
        return self.customer_name


class About(models.Model):
    vision = models.TextField(max_length=5000)
    mission = models.TextField(max_length=5000)
    image_feature = CloudinaryField('image', default='placeholder')
    about = models.TextField(max_length=5000 , null=True)

    def __str__(self):
        return str(self.id)
