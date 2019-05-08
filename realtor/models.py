from django.db import models

# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=255)
    phoneNR = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class RealtorImage(models.Model):
    image = models.CharField(max_length=999)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)