from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required

from food.models import FoodStore ,Category, Cart,Order_fd,OrderItem_fd,Payment

from home.forms.checkout_form import CheckForm

#instamojo
from my_college_store.settings import API_KEY , AUTH_TOKEN
#from instamojo_wrapper import Instamojo



@login_required(login_url='/login/')
def orders(request):
    user= request.user
    context = {
        "order":order
    }
   
    return render(request , template_name='home/orders.html' , context= context)



