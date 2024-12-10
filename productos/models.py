from django.db import models

# Create your models here.

class Snowboard(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=20)

class Ski(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=30)
   
class Antiparras(models.Model):
    marca = models.CharField(max_length=30)
    talle = models.IntegerField()
    modelo = models.CharField(max_length=40) 
    
