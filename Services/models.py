from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=250)
    tagline = models.CharField(max_length=250)
    image = models.FileField(blank=True, null=True)  # FileField for image
    description = models.CharField(max_length=1000)
    url = models.URLField(max_length=300, null=True,blank=True)
    