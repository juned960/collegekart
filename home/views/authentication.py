from home import views
from django.contrib.auth.models import User
from django.db.models import query
from django.http import request
from django.shortcuts import render , HttpResponse , redirect
from home.forms.authforms import CustomerCreationForm , CustomerloginForm
from django.contrib.auth import authenticate, forms ,login as loginUser
from math import floor
from django.contrib.auth.decorators import login_required

from food.models import FoodStore ,Category, Cart
from stationary.models import Cart_st                         #------
from home.models import Extendeduser
from home.forms.checkout_form import CheckForm


from django.views.generic.base import View
#instamojo
from my_college_store.settings import API_KEY , AUTH_TOKEN





#------------------------loginview---start------------------------------#

class LoginView(View):
    def get(self ,request):
        form= CustomerloginForm()
        next_page= request.GET.get('next')
        if next_page is not None:
            request.session['next_page'] = next_page
       
        context={
          'form':form,
        }
        return render(request , template_name='home/login.html', context=context)
 
    def post(self , request):
        form = CustomerloginForm(data=request.POST)    
        if(form.is_valid()):
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            print("========111",user)
            if(user):
                loginUser(request , user)
                print("========111",user)
                #{food ,quantity}
                cart=Cart.objects.filter(user=user)  
                session_cart=[]  
                for c in cart:
                    print(c)
                    obj={
                        'food' : c.foodStore.id,
                        'quantity' : c.quantity
                    }
                    session_cart.append(obj)

                request.session['cart']=session_cart    

                #STATIONARY CART
                cart_st=Cart_st.objects.filter(user=user)    #-------
                session_cart_st=[]
                for c in cart_st:
                    obj_st={
                        'stationary' : c.stationarystore.id,
                        'quantity' : c.quantity
                    }
                    session_cart_st.append(obj_st)

                request.session['cart_st']=session_cart_st



                
                
                next_page = request.session.get('next_page')
                if next_page is None:
                    next_page  = 'homepage'
                return redirect(next_page)

          
        else:
            context={
             'form':form,
            }
            return render(request , template_name='home/login.html', context=context)
#---------------------------------loginview---end------------------------#

"""
def login(request):
    
    if(request.method == 'GET'):
        form= CustomerloginForm()
        next_page= request.GET.get('next')
        if next_page is not None:
            request.session['next_page'] = next_page
       
        context={
          'form':form,
        }
        return render(request , template_name='home/login.html', context=context)
        
    else:
        form = CustomerloginForm(data=request.POST)    
        if(form.is_valid()):
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if(user):
                loginUser(request , user)

                #{food quantity}
                cart=Cart.objects.filter(user=user)
                session_cart=[]
                for c in cart:
                    obj={
                        'food' : c.foodStore.id,
                        'quantity' : c.quantity
                    }
                    session_cart.append(obj)

                request.session['cart']=session_cart
                next_page = request.session.get('next_page')
                if next_page is None:
                    next_page  = 'homepage'
                return redirect(next_page)

          
        else:
            context={
             'form':form,
            }
            return render(request , template_name='home/login.html', context=context)
            """

#-------------------------logout---start-------------------#

def logout(request):
    request.session.clear()
    return redirect('homepage')

#------------------------logout---end--------------------#


#--------------------signup---start-----------------------#

def signup(request):
    if(request.method == 'GET'):
        form=CustomerCreationForm
        context={
           "form":form
        }
        return render(request , template_name='home/signup.html' , context=context)    
    else:
        form=CustomerCreationForm(request.POST)
        
        if(form.is_valid()):
            
            user=form.save()
            user.email = user.username
            user.save()
            phone=request.POST['phone_number']
            print("--------------------------------")
            print(phone)
            print("------------------------------")
            college=request.POST['college_name']
            print(college)
            pincode=request.POST['pincode']
            print(pincode)

            newextendeduser=Extendeduser(user=user)
            newextendeduser.phone_num=phone
            newextendeduser.college_name=college
            newextendeduser.pincode=pincode
            newextendeduser.save()
            
            return redirect('login')
        else:
            context={
              "form":form
            }
            return render(request , template_name='home/signup.html' , context=context)    


#--------------------------signup---end-------------------------#
