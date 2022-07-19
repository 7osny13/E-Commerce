from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class registerUser(models.Model):
    username= models.CharField(max_length=80)
    print(username)