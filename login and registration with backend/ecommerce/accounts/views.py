from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.contrib.auth.models import User
from  accounts.models import *
# Create your views here.
def user_login(request):
   if request=="POST":
    pass
   return render(request,'accounts/login.html')




def user_register(request):
    if request=='POST':
        registerUser.username =request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # repassword=request.POST.get('repassword')
        print("password:"+password,email)
    return render(request,'accounts/register.html')




def user_logout(request):
    pass
