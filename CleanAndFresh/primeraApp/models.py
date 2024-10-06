from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre=models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    