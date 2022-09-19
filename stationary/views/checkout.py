from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required
from my_college_store import settings
from food.models import FoodStore ,Category, Cart
from stationary.models import StationaryStore , Category
from stationary.models import Order_st, OrderItem_st,Payment_st,Cart_st
from home.models import Extendeduser

from home.forms.checkout_form import CheckForm

#instamojo
from my_college_store.settings import API_KEY , AUTH_TOKEN
#from instamojo_wrapper import Instamojo
#API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

#-------------------------------------------------------------------


from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_exempt

import razorpay
#---------------------------------------------------------

def cal_total_payable_amount_st(cart_st):
    total=0
    for c in cart_st :
        discount=c.get('stationary').discount
        price=c.get('stationary').price
        sale_price= floor(price -( price * (discount / 100)))
        total = total+total_of_single_product

    return total    


def buynow_total_payable_amount_st(stationary):
    total=0
    after_discount=stationary.price - (stationary.price*stationary.discount / 100)
    after_discount=floor(after_discount)
    return after_discount
      

#---------------------------------------------------------------------

########################################################..............................(9).......................checkout
@login_required(login_url='/login/')
def checkout(request):
    if request.method == 'GET':
       #get request
        form= CheckForm()
        cart_st=request.session.get('cart_st')
        if cart_st is None:
            cart_st=[]

       

        user=None
        if request.user.is_authenticated:
            user=request.user
        

        exu=Extendeduser.objects.filter(user=user) 

        return render(request ,'stationary/checkout.html' ,{"form" : form , "cart_st" : cart_st,"exu":exu})
    else:
        #post request
        print("000000000000000000000000000000000000")

        form = CheckForm(request.POST)
     
        user=None
        if request.user.is_authenticated:
            user=request.user

        if form.is_valid():
            #payment
            cart_st= request.session.get('cart_st')
            if cart_st is None:
                cart_st=[]
            for c in cart_st :
                stationary_id= c.get('stationary') 
                stationary = StationaryStore.objects.get(id=stationary_id)
                c['stationary']=stationary 


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
            total=cal_total_payable_amount_st(cart_st)
            

            order =Order_st()
            order.college=college
            order.pincode=pincode
            order.phone=phone
            order.payment_method=payment_method
            order.total=total
            order.order_status="PENDING"
            order.user=user
            order.save()

            #saving order_item
            for c in cart_st:
                order_item = OrderItem_st()
                order_item.order = order
                stationary=c.get('stationary')
                order_item.price = floor(stationary.price -( stationary.price * (stationary.discount / 100)))
                order_item.quantity = c.get('quantity')
                order_item.stationarystore = stationary
                order_item.save()

            # creating payment
            #for Online payment
            if payment_method == "ONLINE":

                razorpay_client  = razorpay.Client(auth=(settings.keyid, settings.keySecret))

                callback_url = 'http://'+ str(get_current_site(request))+"/stationary/handlerequest/"
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
                payment = Payment_st()
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



                """
                response = API.payment_request_create(
                amount=order.total,
                purpose='payment for buying online product on collegebag',
                send_email=True,
                buyer_name=f'{user.first_name} {user.last_name}',
                email=user.email,
                redirect_url="http://localhost:8000/stationary/validate_payment_st"
                )
                print( response['payment_request'])

                payment_request_id = response['payment_request']['id']
                url = response['payment_request']['longurl']

                payment = Payment_st()
                payment.order = order
                payment.payment_request_id = payment_request_id
                payment.save()

                return redirect(url) 

                """
            #for Case on delivery    
            else:
                order.order_status= 'PLACED'
                order.save()

                payment = Payment_st()
                payment.order = order
                payment.payment_request_id = 'none'
                payment.payment_id = 'none'
                payment.payment_status =  'none'
                payment.razorpay_signature='none'
                payment.save()
                
                cart_st =[]
                request.session['cart_st'] = cart_st

                Cart_st.objects.filter(user = user).delete()

                return redirect('my_orders')   
                
               

        else:
            return redirect('/checkout/')    



@login_required(login_url='/login/')  #----
def buynow_st(request , slug):
    stationary = StationaryStore.objects.get(slug=slug)
    if request.method == 'GET':
       #get request
        form= CheckForm()

        user=None
        if request.user.is_authenticated:
            user=request.user
        

        exu=Extendeduser.objects.filter(user=user) 
        
       
        return render(request ,'stationary/buynow.html' ,{"form" : form , "stationary" : stationary,"exu":exu})
    else:
        #post request
        print("jjjjjjjjjjjjjjjjjjjj")

        form = CheckForm(request.POST)
        
     
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
            total=buynow_total_payable_amount_st(stationary)
          
           # print(shipping_address , phone , payment_method ,total)

            order =Order_st()
            order.college=college
            order.pincode=pincode
            order.phone=phone
            order.payment_method=payment_method
            order.total=total
            order.order_status="PENDING"
            order.user=user
            order.save()

            #saving order_item
            
            order_item = OrderItem_st()
            order_item.order = order  
            order_item.price = floor(stationary.price -( stationary.price * (stationary.discount / 100)))
            order_item.quantity = '1'
            order_item.stationarystore = stationary
            order_item.save()

            # creating payment
            #for Online payment
            if payment_method == "ONLINE":

                razorpay_client  = razorpay.Client(auth=(settings.keyid, settings.keySecret))

                callback_url = 'http://'+ str(get_current_site(request))+"/stationary/handlerequest_buynow/"
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
                payment = Payment_st()
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


                """
                response = API.payment_request_create(
                amount=order.total,
                purpose='payment for buying online product on collegebag',
                send_email=True,
                buyer_name=f'{user.first_name} {user.last_name}',
                email=user.email,
                redirect_url="http://localhost:8000/stationary/buynowvalidate_payment"
                )
               

                payment_request_id = response['payment_request']['id']
                url = response['payment_request']['longurl']

                payment = Payment_st()
                payment.order = order
                payment.payment_request_id = payment_request_id
                payment.save()

                return redirect(url) 

                """
            #for Case on delivery    
            else:
                order.order_status= 'PLACED'
                order.save()
                payment = Payment_st()
                payment.order = order
                payment.payment_request_id = 'none'
                payment.payment_id = 'none'
                payment.payment_status =  'none'
                payment.razorpay_signature='none'
                payment.save()
                
                return redirect('my_orders')   
                
               

        else:
            return redirect('/stationary/checkout/')    



    
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
                order_db=Payment_st.objects.get(payment_request_id=order_id)
                
            except:
                return HttpResponse("5052 NOT Found")    
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
                    cart_st =[]
                    request.session['cart_st'] = cart_st
                    Cart_st.objects.filter(user = user).delete()

                    return redirect('my_orders') 
                except:
                    order_db.payment_status='failed'
                    order_db.save()
                    return render(request , 'stationary/payment_failed.html')
            else:
                order_db.payment_status='failed'
                order_db.save()
                return render(request , 'stationary/payment_failed.html')
        except:
           
            return HttpResponse("5051 Not Found")
      

         
@csrf_exempt
def handlerequest_buynow(request):
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
                order_db=Payment_st.objects.get(payment_request_id=order_id)
                
            except:
                return HttpResponse("5052 NOT Found")    
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
                    return render(request , 'stationary/payment_failed.html')
            else:
                order_db.payment_status='failed'
                order_db.save()
                return render(request , 'stationary/payment_failed.html')
        except:
           
            return HttpResponse("5051 Not Found")
      