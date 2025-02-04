from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    address = models.TextField(blank=True,null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)

    #add other fields
    def __str__(self):
        return self.email


