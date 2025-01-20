from django.db import models

# Create your models here.


class Costumers(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=9)


class Items(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()


class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField(max_length=30)
    status_delivery = models.BooleanField()