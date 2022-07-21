from django import forms
from .models import *
from django.forms import ModelForm

class Loginform(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )