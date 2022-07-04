
from django.db import models

# Create your models here.


class pizza (models.Model):
    nombre= models.CharField(max_length=30, unique=True)
    ingredientes=models.CharField(max_length= 60)
    precio=models.FloatField()
    apto_delivery=models.BooleanField()
    vegana=models.BooleanField()
    foto =  models.ImageField(upload_to= 'pizzas', blank=True, null=True)

class empanada (models.Model):
    nombre= models.CharField(max_length=30, unique=True) 
    ingredientes=models.CharField(max_length= 60)
    precio=models.FloatField()
    apto_delivery=models.BooleanField()
    foto =  models.ImageField(upload_to= 'empanadas', blank=True, null=True)

class bebida (models.Model):
    nombre=models.CharField(max_length=30, unique=True)
    precio=models.FloatField()
    apto_delivery=models.BooleanField()
    foto =  models.ImageField(upload_to= 'bebidas', blank=True, null=True)

class postre (models.Model):
    nombre=models.CharField(max_length=30, unique=True)
    precio=models.FloatField()
    apto_delivery=models.BooleanField()
    gluten_free=models.BooleanField()
    foto =  models.ImageField(upload_to= 'postres', blank=True, null=True)