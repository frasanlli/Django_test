from django.db import models

# Create your models here.
#to add new features and use them, first we need to repeat migrations
#python manage.py makemigrations
#python manage.py migrate

class Costumers(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    #To enable blank or null fields set properties (blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=9)


class Items(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f"Name: {self.name}. Category: {self.category}. Price: {self.price}"


class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField(max_length=30)
    status_delivery = models.BooleanField()
