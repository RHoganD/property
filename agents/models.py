from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    image = CloudinaryField('image', default='placeholder')
 

    def __str__(self):
        return self.name
