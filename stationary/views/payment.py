from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required

from food.models import FoodStore ,Category, Cart

from stationary.models import OrderItem_st,Order_st,Payment_st,Cart_st
from home.forms.checkout_form import CheckForm

#instamojo
from my_college_store.settings import API_KEY , AUTH_TOKEN
#from instamojo_wrapper import Instamojo
#API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');


########################################################..............................(10)..................validatePayment
def validatePayment_st(request):
    print("juned juned juned juned juned junedjuned juned")
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
            payment = Payment_st.objects.get(payment_request_id =payment_request_id)
            payment.payment_id = payment_id
            payment.payment_status =  status
            payment.save()
            order= payment.order
            order.order_status= 'PLACED'
            order.save()

            cart_st =[]
            request.session['cart_st'] = cart_st

            Cart_st.objects.filter(user = user).delete()

            return redirect('orders') 
         
        except:
             return render(request , 'stationary/payment_failed.html')

    else:
         return render(request , 'stationary/payment_failed.html')
        #//return error page    




########################################################..............................(10)..................validatePayment


def buynow_validatePayment_st(request):  #----
    user = None
    if request.user.is_authenticated:
        user=request.user

    print(user)        
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    status = response.get('payment_request').get('payment').get('status')

    if status != "Failed":
        print('payment Succsess')
        try:
            payment = Payment_st.objects.get(payment_request_id =payment_request_id)
            payment.payment_id = payment_id
            payment.payment_status =  status
            payment.save()
            order= payment.order
            order.order_status= 'PLACED'
            order.save()

            

            return redirect('/stationary/orders_st/') 
         
        except:
             return render(request , 'home/payment_failed.html')

    else:
         return render(request , 'home/payment_failed.html')
        #//return error page  
