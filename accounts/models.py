from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    gender= models.CharField(choices=('Man','Female'), max_length=5)
    age= models.PositiveIntegerField(null=True, blank=True)