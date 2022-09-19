from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required


from food.models import FoodStore ,Category, Cart,OrderItem_fd,Order_fd,Payment
from home.models import  Extendeduser
from home.forms.checkout_form import CheckForm
from my_college_store import settings

from stationary.models import StationaryStore , Order_st ,OrderItem_st ,Payment_st ,Cart_st

#instamojo
from my_college_store.settings import API_KEY , AUTH_TOKEN
#from instamojo_wrapper import Instamojo
#API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');
 

#---------------------------------------------------------


import razorpay





#-------------------------------------------------------------------
def cal_total_payable_amount(cart):
    total=0
    for c in cart :
        discount=c.get('food').discount
        price=c.get('food').price
        
        total = total+total_of_single_product

    return total    


def buynow_total_payable_amount(food):
    total=0
    after_discount=food.price - (food.price*food.discount / 100)
    after_discount=floor(after_discount)
    return after_discount
      


#---------------------------------------------------------------------


#------------------------------checkout---start---------food----------#
@login_required(login_url='/login/')
def checkout(request):
    if request.method == 'GET':
       #get request
        form= CheckForm()
        cart=request.session.get('cart')
        if cart is None:
            cart=[]

      
      
        user=None
        if request.user.is_authenticated:
            user=request.user
        

        exu=Extendeduser.objects.filter(user=user)   #---

        
        

        return render(request ,'food/checkout.html' ,{"form" : form , "cart" : cart,"exu":exu})
    else:
        #post request

        form = CheckForm(request.POST)
     
        user=None
        if request.user.is_authenticated:
            user=request.user

        if form.is_valid():
            #payment
            cart= request.session.get('cart')
            if cart is None:
           
  
            
            exu=Extendeduser.objects.filter(user=user) 

            college = None
            pincode=None
            phone = None
            for ex in exu:
                college=ex.college_name
                pincode=ex.pincode
                phone=ex.phone_num
           
   
            #college = form.cleaned_data.get('college')
            #pincode=form.cleaned_data.get('pincode')
            #phone = form.cleaned_data.get('phone')
            payment_method= form.cleaned_data.get('payment_method')
            total=cal_total_payable_amount(cart)
            

            order =Order_fd()
            order.college=college
          
            order.save()

            #saving order_item
            for c in cart:
                
                order_item.foodstore = food
                order_item.save()

            # creating payment
            #for Online payment
            if payment_method == 'ONLINE':
                
                razorpay_client  = razorpay.Client(auth=(settings.keyid, settings.keySecret))

            
                print(callback_url)

                data={
                    'amount':(order.total)*100,
                    "currency": "INR",
                    'receipt': "shoping on clgkart",
                    'notes': {
                        "name":f'{user.first_name} {user.last_name}',
                        "payment for":"online shoping from clgkart"
                    }
                }
                razorpay_order=razorpay_client .order.create(data=data)
                print(razorpay_order['id'])
                payment = Payment()
                payment.order = order
                payment.payment_request_id =razorpay_order['id']
                payment.save()
                context={
                    'order':order,
                    'orders_id' :razorpay_order['id'],
                    'razorpay_merchant_id': settings.keyid ,
                   
                    'user_name':user.get_full_name ,
                    'phone':phone,
                    'email':user.email
                    
                    
                }

                return render(request ,'food/payment.html' ,context=context)






            #for Case on delivery    
            else:
                order.order_status= 'PLACED'
                order.save()

                payment.save()
                
                cart =[]
                request.session['cart'] = cart

                Cart.objects.filter(user = user).delete()

                return redirect('my_orders')   
          
        else:
            return redirect('/foods/checkout/')    
#------------------------------checkout---end---------food----------#



#------------------------------buynow---start---------food----------#
@login_required(login_url='/login/')  
def buynow(request , slug):
    food = FoodStore.objects.get(slug=slug)
    if request.method == 'GET':
       #get request
        form= CheckForm()

        user=None
        if request.user.is_authenticated:
            user=request.user
        

        exu=Extendeduser.objects.filter(user=user) 
        
       
     
        user=None
        if request.user.is_authenticated:
            user=request.user

        if form.is_valid():
            #payment 


            exu=Extendeduser.objects.filter(user=user) 

            college = None
            pincode=None
            phone = None
            for ex in exu:
                college=ex.college_name
                pincode=ex.pincode
                phone=ex.phone_num


            #college= form.cleaned_data.get('college')
            #pincode=form.cleaned_data.get('pincode')
            #phone = form.cleaned_data.get('phone')
            payment_method= form.cleaned_data.get('payment_method')
            total=buynow_total_payable_amount(food)
          
          
            print("p33333333333333333333")
            o
            
            order_item = OrderItem_fd()
            order_item.order = order  
            order_item.price = floor(food.price -( food.price * (food.discount / 100)))
            order_item.quantity = '1'
            order_item.foodstore = food
            order_item.save()

            # creating payment
            #for Online payment
            if payment_method == "ONLINE":
                razorpay_client  = razorpay.Client(auth=(settings.keyid, settings.keySecret))

                callback_url = 'http://'+ str(get_current_site(request))+"/foods/handlerequest_buynow/"
                print(callback_url)

                data={
                    'amount':(order.total)*100,
                    
                razorpay_order=razorpay_client .order.create(data=data)
                print(razorpay_order['id'])
                payment = Payment()
                payment.order = order
                payment.payment_request_id =razorpay_order['id']
                payment.save()
                context={
                    'order':order,
                    'orders_id' :razorpay_order['id'],
                    'razorpay_merchant_id': settings.keyid ,
                    'callback_url':callback_url,
                    'user_name':user.get_full_name ,
                    'phone':phone,
                    'email':user.email
                    
                    
                }

                return render(request ,'food/payment.html' ,context=context)



            #for Case on delivery    
            else:
                order.order_status= 'PLACED'
                order.save()
                payment = Payment()
                payment.order = order
                payment.payment_request_id = 'none'
                payment.payment_id = 'none'
                payment.payment_status =  'none'
                payment.razorpay_signature='none'
                payment.save()
                
                return redirect('my_orders')   
                
               

        else:
            return redirect('/foods/checkout/')    

#------------------------------buynow---end---------food----------#







    
@csrf_exempt
def handlerequest(request):
    user = None
    if request.user.is_authenticated:
        user=request.user
    razorpay_client  = razorpay.Client(auth=(settings.keyid, settings.keySecret))
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id','')
            order_id=request.POST.get('razorpay_order_id','')
            signature=request.POST.get('razorpay_signature','')
            params_dict ={
                'razorpay_order_id':order_id,
                'razorpay_payment_id':payment_id,
                'razorpay_signature':signature
            }
            try:
                order_db=Payment.objects.get(payment_request_id=order_id)
                
            except:
                return HttpResponse("505 NOT Found")    
            order_db.payment_id=payment_id
            order_db.razorpay_signature=signature
            
            order_db.save()
            order= order_db.order
            order.order_status= 'PLACED'
            order.save()
            
            result = razorpay_client.utility.verify_payment_signature(params_dict)
                                  
          ()

                    return redirect('my_orders') 
                except:
                    order_db.payment_status='failed'
                    order_db.save()
                    return render(request , 'food/payment_failed.html')
            else:
                order_db.payment_status='failed'
                order_db.save()
                return render(request , 'food/payment_failed.html')
        except:
           
            return HttpResponse("505 Not Found")
            

""""""


@csrf_exempt
def handlerequest_buynow(request):
    user = None
    if request.user.is_authenticated:
        user=request.user
    razorpay_client  = razorpay.Client(auth=(settings.keyid, settings.keySecret))
    if request.method == "POST":
        try:
            
            :
                order_db=Payment.objects.get(payment_request_id=order_id)
                
            except:
                return HttpResponse("505 NOT Found")    
            order_db.payment_id=payment_id
            order_db.razorpay_signature=signature
            
            order_db.save()
            order= order_db.order
            order.order_status= 'PLACED'
            order.save()
            
            result = razorpay_client.utility.verify_payment_signature(params_dict)
                                  
            print(result)
            if result==None:                
                try:
                    #razorpay_client.payment.capture(payment_id, amount, {"currency":"payment_currency"})
                    order_db.payment_status='credit'
                    order_db.save()
                    

                    return redirect('my_orders') 
                except:
                    order_db.payment_status='failed'
                    order_db.save()
                    return render(request , 'food/payment_failed.html')
            else:
                order_db.payment_status='failed'
                order_db.save()
                return render(request , 'food/payment_failed.html')
        except:
           
            return HttpResponse("505 Not Found")
            



