from turtle import update
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

#this function to make username==email  presave on db by send Signal when submit to login with email as username
def updateUser(sender,instance,**kwargs):
    user=instance
    if user.email  != '':
        user.username= user.email
pre_save.connect(updateUser,sender=User)