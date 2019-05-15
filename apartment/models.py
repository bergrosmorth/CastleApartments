from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.country


class Apartment(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.IntegerField()
    size = models.FloatField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
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


class BuyerInformation(models.Model):
    SSN = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    cardnumber = models.CharField(max_length=16)
    cvc = models.CharField(max_length=3)
    month = models.CharField(max_length=10)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.SSN


