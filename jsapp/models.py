from django.db import models

# Create your models here.

class coursesavedb(models.Model):
    cname = models.CharField(max_length=100,null=True,blank=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="Course Image",null=True,blank=True)