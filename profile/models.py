from django.db import models
from django.contrib.auth.models import User
from apartment.models import Apartment


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    favorite_apartments = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    image = models.CharField( max_length=999 )


