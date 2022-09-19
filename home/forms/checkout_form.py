from email import message
from re import I
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from food.models import Order_fd
from home.models import Contact_us

#>>>>--------------Checkform---start---------------#
"""
class CheckForm(forms.ModelForm):
    class Meta:
        model=Order
        fields = ['college','pincode','phone','payment_method']
        
"""
class CheckForm(forms.ModelForm):
    class Meta:
        model=Order_fd
        fields = ['payment_method']

#--------------CustomerCreationform---end---------------<<<<#
class Contact_us_form(forms.ModelForm):
    class Meta:
        model=Contact_us
        fields=['name','email','phone','subject','message']
