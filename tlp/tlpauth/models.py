from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=55, unique=True, null=True) 
    contact = models.CharField(max_length=14)  
    ProfilePic = models.TextField(null=False,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQK5RUB36B772FIiK9BvNV_cQaxJB7wxfFz7w&usqp=CAU')
    full_names = models.TextField(null=True)
    gender = models.CharField(max_length=55,null=True)
    email = models.EmailField(default=True)
    Date = models.DateField(auto_now_add=True)
    uid = models.TextField(null=True)
   