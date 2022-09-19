from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required



from home.forms.checkout_form import CheckForm
from food.models import Order_fd
from stationary.models import Order_st
#instamojo
from my_college_store.settings import API_KEY , AUTH_TOKEN
#from instamojo_wrapper import Instamojo



@login_required(login_url='/login/')
def my_orders(request):
    user= request.user
    order_for_food= Order_fd.objects.filter(user=user).order_by('-date').exclude(order_status = 'PENDING')
    context = {
        "order_for_food":order_for_food ,

    }
   
    return render(request , template_name='home/my_orders.html' , context= context)



