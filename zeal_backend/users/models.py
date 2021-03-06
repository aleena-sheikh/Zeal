from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique = True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique = True, null=True)
    profile_pic = models.ImageField(upload_to ='user_profile_pictures/', default='user_profile_pictures/default_user.jpeg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]


class PasswordReset(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
