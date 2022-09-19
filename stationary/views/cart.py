from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required

from food.models import FoodStore ,Category, Cart
from stationary.models import StationaryStore ,Cart_st,Category

from home.forms.checkout_form import CheckForm

#instamojo

from my_college_store.settings import API_KEY , AUTH_TOKEN
#from instamojo_wrapper import Instamojo


def cart_st(request):
    cart_st=request.session.get('cart_st')
    if cart_st is None:
        cart_st=[]
    for c in cart_st:
        stationary_id = c.get('stationary')    
        stationary = StationaryStore.objects.get(id=stationary_id)
        c['stationary']=stationary
    return render(request , template_name='stationary/cart_st.html', context={"cart_st":cart_st} )



def clear_cart(request):               #-----
    user=None
    if request.user.is_authenticated:
        user=request.user

    cart_st =[]
    request.session['cart_st'] = cart_st

    Cart_st.objects.filter(user = user).delete()    
    
    return_url = request.GET.get('return_url')
    return redirect(return_url)



def add_to_cart_st(request , slug):

    user=None
    if request.user.is_authenticated:
        user = request.user
    cart_st=request.session.get('cart_st')

    
    if cart_st is None:
        cart_st=[]
    
    flag = True
    for cart_obj in cart_st:
        st_id = cart_obj.get('stationary')
        if st_id==stationary.id:
            
            flag = False
            cart_obj['quantity'] = cart_obj['quantity'] + 1

    if flag:        
        cart_obj = {
            'stationary':stationary.id,
            'quantity': 1      
        }    
        cart_st.append(cart_obj)
    if user is not None:        
        existing = Cart_st.objects.filter(user=user , stationarystore = stationary)
        if len(existing)>0:
            obj=existing[0]
            obj.quantity= obj.quantity+1
            obj.save()
        else:
            c=Cart_st()
            c.user= user
            c.stationarystore=stationary
            c.quantity=1
            c.save()    
            
        
        
    request.session['cart_st']=cart_st

    return_url = request.GET.get('return_url')
    return redirect(return_url)