from home.views.home import home
from home.views.authentication import LoginView, signup , logout 
from home.views.my_orders import my_orders
from home.views.product_page import show_food_product
from home.views.my_cart import my_cart
from home.views.footer import team, career, contact_us, term_and_condition ,privacy_policy , return_policy , about_us  

from django.contrib.auth.views import PasswordResetView ,PasswordResetDoneView ,PasswordResetConfirmView ,PasswordResetCompleteView

