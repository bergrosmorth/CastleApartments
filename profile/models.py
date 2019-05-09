from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class ProfileImage(models.Model):
    image = models.CharField(max_length=999)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
