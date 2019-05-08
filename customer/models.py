from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phoneNR = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class CustomerImage(models.Model):
    image = models.CharField(max_length=999)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)