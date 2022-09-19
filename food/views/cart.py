from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required

from food.models import FoodStore ,Category, Cart

from home.forms.checkout_form import CheckForm
from stationary.models import StationaryStore
#instamojo

from my_college_store.settings import API_KEY , AUTH_TOKEN




#----------------------cart---start-------------------#

def cart(request):
    print("---------------------------")
    cart=request.session.get('cart')
    if cart is None:
        cart=[]
    for c in cart:
        food_id = c.get('food')    
        food = FoodStore.objects.get(id=food_id)
        c['food']=food

   

    context={
        'cart':cart,
       
    }    
    return render(request , template_name='home/cart.html', context=context )

#-------------------------------cart---end----------------#


#------------------------------clearcart---start----------#

def clear_cart(request):              
    user=None
    if request.user.is_authenticated:
        user=request.user

    cart =[]
    request.session['cart'] = cart

    
    return_url = request.GET.get('return_url')
    return redirect(return_url)

#---------------------clearcart---end-----------------------#



#--------------------add_to_cart----start------------------#

def add_to_cart(request , slug):

    user=None
    if request.user.is_authenticated:
        user = request.user
    food = FoodStore.objects.get(slug=slug)
    cart=request.session.get('cart')

    
    if cart is None:
        cart=[]
    
    flag = True
    for cart_obj in cart:
        f_id = cart_obj.get('food')
        if f_id==food.id:
            
            flag = False
         

    if flag:        
        cart_obj = {
            'food':food.id,
            'quantity': 1      
        }    
        cart.append(cart_obj)
    if user is not None:        
      
        if len(existing)>0:
            
            obj.quantity= obj.quantity+1
            obj.save()
        else:
            c=Cart()
            c.user= user
            c.foodStore=food
            c.quantity=1
            c.save()    
            
        
        
    request.session['cart']=cart

    return_url = request.GET.get('return_url')
    return redirect(return_url)
#------------------add_to_cart---end-----------------#





    