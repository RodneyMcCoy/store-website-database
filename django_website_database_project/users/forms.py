from dataclasses import field
import email
import imp
from re import T
from django import forms
from django.db import transaction
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from store.models import User, Customer, Vendor

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    

class ChooseRegisterTypeForm(forms.Form):
    choice = forms.ChoiceField(choices=([('', ''), ('Customer', 'Customer'), ('Vendor', 'Vendor')]), label='Sign up as')
    
    


class CustomerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class VendorRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    