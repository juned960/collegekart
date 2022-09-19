from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required

from food.models import FoodStore ,Category, Cart

from stationary.models import StationaryStore
from home.forms.checkout_form import CheckForm


#instamojo

from my_college_store.settings import API_KEY , AUTH_TOKEN
#from instamojo_wrapper import Instamojo



def my_cart(request):
    #cart -----------------
    cart=request.session.get('cart')
    if cart is None:
        cart=[]
    for c in cart:
        food_id = c.get('food')    
        c['food']=food

    #cart_st -----------------
    cart_st=request.session.get('cart_st')  
    if cart_st is None:
        cart_st=[]
    for c in cart_st:
        stationary_id = c.get('stationary')    
        stationary = StationaryStore.objects.get(id=stationary_id)
        c['stationary']=stationary

   



    context={
        'cart_st':cart_st ,
        'cart':cart,
    }  
    return render(request , template_name='home/my_cart.html', context=context )






    