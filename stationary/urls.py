
from django.urls import path
from stationary.views import handlerequest,handlerequest_buynow,sthome ,show_stationary_product ,add_to_cart_st ,cart_st,checkout,validatePayment_st,clear_cart,buynow_st,buynow_validatePayment_st

urlpatterns = [
    path('' , sthome),
    path('product/<str:slug>' , show_stationary_product),
    path('addtocart_st/<str:slug>' , add_to_cart_st),
    path('cart_st/' ,cart_st),
    path('clearcart/' , clear_cart),     
    path('checkout/',checkout),
    path('validate_payment_st/' ,validatePayment_st) ,
    path('buynowvalidate_payment/' ,buynow_validatePayment_st) ,
    path('buynow/product/<str:slug>/' ,buynow_st) ,
    path('handlerequest/',handlerequest),
    path('handlerequest_buynow/',handlerequest_buynow)
]

