from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES=(
        ('Man','Man'),
        ('Female','Female'),
        )

    gender= models.CharField(choices=GENDER_CHOICES, max_length=7,null=False, blank=False)
    age= models.PositiveIntegerField(null=True, blank=True)