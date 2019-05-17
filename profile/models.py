from django.db import models
from django.contrib.auth.models import User
from apartment.models import Apartment


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=999, blank=True)
    phone = models.IntegerField(blank=True)
    address = models.CharField(max_length=999, blank=True)
    email = models.CharField(max_length=999, blank=True)
    image = models.CharField( max_length=999, default='https://www.autourdelacom.fr/wp-content/uploads/2018/03/default-user-image.png', blank=True)


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search = models.CharField(max_length=999)