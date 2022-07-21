from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20, unique=True)
    email=models.EmailField(max_length=50,null=False)
    password=models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    Birthdate = models.DateField(null=True)
    phone_number =  models.CharField(null=True,max_length=11)
    profile_pic = models.ImageField(upload_to='profileimage', blank=False)
    country = models.CharField(max_length=20,null=True )
    facebook_profile = models.CharField(null=True,max_length=20)