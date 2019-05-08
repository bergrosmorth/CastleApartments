from django.db import models

# Create your models here.


class Apartment(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.IntegerField()
    country = models.CharField(max_length=255)
    price = models.IntegerField()
    type = models.CharField(max_length=255)
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
