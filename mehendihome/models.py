from distutils.command.upload import upload
from operator import truediv
from pyexpat import model
from statistics import mode

from urllib import request
from django.db import models
import uuid

# Create your models here.

class mehendi(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
   
    
   
    mehendi_style = models.CharField(max_length=122)
    mehendi_desc = models.CharField(max_length=122)
    mehendi_time = models.TimeField()
    
    
    image = models.ImageField(upload_to="mehendi/images")
    mehendi_date = models.DateTimeField()
   
    
    

    def __str__(self)  :
        return self.mehendi_style

class rangoli(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    rangoli_style = models.CharField(max_length=122)
    rangoli_desc = models.CharField(max_length=122)
    rangoli_date = models.DateTimeField()
    image = models.ImageField(upload_to="rangoli/images")
    
    

    def __str__(self)  :
        return self.rangoli_style


class appoinment(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    time = models.DateTimeField()
    number = models.CharField(max_length=122)

    def __str__(self):
        return self.email