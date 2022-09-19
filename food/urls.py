#from django.contrib.auth import views as auth_views  #-----
#from django.contrib.auth.views import PasswordResetView ,PasswordResetDoneView ,PasswordResetConfirmView , PasswordResetCompleteView  #-----
from django.urls import path
from food.views import checkout,handlerequest,handlerequest_buynow, home ,cart , show_food_product , add_to_cart , checkout , clear_cart 
from food.views import buynow  



urlpatterns = [
    path('addtocart/<str:slug>' , add_to_cart),
    path('clearcart/' , clear_cart),           #------
    path('product_details/<str:slug>' , show_food_product),
    path('buynow/product/<str:slug>/' , buynow),   #----

    
    path('' ,home , name='homepage'),
    
    path('cart/' ,cart),
    





  

]
