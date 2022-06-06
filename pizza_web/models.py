from django.db import models

# Create your models here.
class pizza (models.Model):
    nombre= models.CharField(max_length=30, unique=True)
    ingredientes=models.CharField(max_length= 60)
    precio=models.FloatField()
    apto_delivery=models.BooleanField()
    vegana=models.BooleanField()

class empanada (models.Model):
    nombre= models.CharField(max_length=30, unique=True) 
    ingredientes=models.CharField(max_length= 60)
    precio=models.FloatField()
    apto_delivery=models.BooleanField()

class bebida (models.Model):
    nombre=models.CharField(max_length=30, unique=True)
    precio=models.FloatField()
    apto_delivery=models.BooleanField()

class postre (models.Model):
    nombre=models.CharField(max_length=30, unique=True)
    precio=models.FloatField()
    apto_delivery=models.BooleanField()
    gluten_free=models.BooleanField()