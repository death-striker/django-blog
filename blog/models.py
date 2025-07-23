from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RegisterUser(AbstractUser):

    email= models.EmailField(unique= True)
    username=models.CharField(unique=True)
    phone_number = models.CharField(unique= True,max_length= 10, blank=False)
    address = models.CharField( blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']

    def __str__(self):
        return self.email




