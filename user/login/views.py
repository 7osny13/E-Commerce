from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from .models import User
from .forms import *
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html', {})
    else:
        user = User.objects.filter(email=request.POST['email'], password=request.POST['password'])
        if (len(user) != 0):
            request.session['password'] = user[0].password
            request.session['email'] = user[0].email
            request.session['username'] = user[0].username


            # return redirect('/project/home')
            # return HttpResponse('saved')
            return render(request, 'home.html', )

        else:
            return HttpResponseRedirect('/login')

        return render(req, 'users/login.html', {'error': 'invalid'})

def HomeView(request):
    return render(request, 'home.html', )

