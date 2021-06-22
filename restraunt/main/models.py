from django.db import models

# Create your models here.
class pizza(models.Model):
    img = models.ImageField(upload_to='pics/pizza')
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=10000)
    price = models.IntegerField(null=False)

class salad(models.Model):
    img = models.ImageField(upload_to='pics/salad')
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=10000)
    price = models.IntegerField(null=False)

class noodles(models.Model):
    img = models.ImageField(upload_to='pics/noodles')
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=10000)
    price = models.IntegerField(null=False)