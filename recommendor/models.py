from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class UserPrefrence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prefrence = ArrayField(models.CharField(max_length=255))