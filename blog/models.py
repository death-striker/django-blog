from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class RegisterUser(AbstractUser):

    email= models.EmailField(unique= True)
    username=models.CharField(blank=True, null=True,unique=True)
    phone_number = models.CharField(unique= True,max_length= 10, blank=False)
    address = models.CharField( blank=True, null=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name' , 'username']

    def __str__(self):
        return self.email

class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title





