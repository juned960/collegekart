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
#API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');


########################################################..............................(10)..................validatePayment
def validatePayment(request):
    user = None
    if request.user.is_authenticated:
        user=request.user

    print(user)        
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    print(payment_request_id ,payment_id)
    status = response.get('payment_request').get('payment').get('status')

    if status != "Failed":
        print('payment Succsess')
        try:
            payment = Payment.objects.get(payment_request_id =payment_request_id)
            payment.payment_id = payment_id
            payment.payment_status =  status
            payment.save()
            order= payment.order
            order.order_status= 'PLACED'
            order.save()

            cart =[]
            request.session['cart'] = cart

            Cart.objects.filter(user = user).delete()

            return redirect('orders') 
         
        except:
             return render(request , 'home/payment_failed.html')

    else:
         return render(request , 'home/payment_failed.html')
        #//return error page    




########################################################..............................(10)..................validatePayment


def buynowvalidatePayment(request):  #----
    user = None
    if request.user.is_authenticated:
        user=request.user

    print(user)        
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    print(payment_request_id ,payment_id)
    response = API.payment_request_payment_status(payment_request_id , payment_id)
    status = response.get('payment_request').get('payment').get('status')

    if status != "Failed":
        print('payment Succsess')
        try:
            payment = Payment.objects.get(payment_request_id =payment_request_id)
            payment.payment_id = payment_id
            payment.payment_status =  status
            payment.save()
            order= payment.order
            order.order_status= 'PLACED'
            order.save()

            

            return redirect('orders') 
         
        except:
             return render(request , 'home/payment_failed.html')

    else:
         return render(request , 'home/payment_failed.html')
        #//return error page  
