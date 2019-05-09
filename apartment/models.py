from django.db import models
from django.contrib.auth.models import User


class Apartment(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.IntegerField()
    country = models.CharField(max_length=255)
    price = models.IntegerField()
    rooms = models.IntegerField()
    description = models.CharField(max_length=999, blank=True)
    realator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
