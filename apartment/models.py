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


def get_image_filename(instance, filename):
    id = instance.apartment.id
    return "post_images/%s" % (id)


class ApartmentImage(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)


class BuyerInformation(models.Model):
    SSN = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    cardnumber = models.CharField(max_length=16)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    cvc = models.CharField(max_length=3)

    def __str__(self):
        return self.SSN

class OpenHouse(models.Model):
    address = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=15)

