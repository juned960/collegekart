from django.contrib.auth.models import User
#from django.core import paginator
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required

from food.models import FoodStore ,Category, Cart , Carousel

from home.forms.checkout_form import CheckForm

from django.core.paginator import Paginator

from urllib.parse import urlencode


#instamojo
from my_college_store.settings import API_KEY , AUTH_TOKEN





def home(request):
    query=request.GET
    foodstore = []
    carousel =[]
    carousels=Carousel.objects.all()
    foodstore=FoodStore.objects
    
   1

    
    if categorys!='' and categorys is not None:
        foodstore=foodstore.filter(category__slug=categorys)
    else:
        foodstore = foodstore.all()



    category=Category.objects.all()

    

    paginator = Paginator(foodstore ,8)
    page_object = paginator.get_page(page)

    query = request.GET.copy()
    query['page'] = ''
    pageurl = urlencode(query)
    

    context={
        'page_object':page_object,                #'foodstore':foodstore
        'category':category,
        'pageurl':pageurl,
  
    }
    return render(request , template_name='food/index.html' , context=context)
