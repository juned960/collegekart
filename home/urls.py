#from django.contrib.auth import views as auth_views  #-----
#from django.contrib.auth.views import PasswordResetView ,PasswordResetDoneView ,PasswordResetConfirmView , PasswordResetCompleteView  #-----
from django.urls import path
from home.views import team, my_cart , my_orders,term_and_condition ,privacy_policy  , return_policy , about_us , contact_us , career
from home.views import PasswordResetView ,PasswordResetDoneView ,PasswordResetConfirmView ,PasswordResetCompleteView



urlpatterns = [

    
    path('' ,home , name='homepage'),
    path('my_orders/' ,my_orders , name='my_orders'),   #------
    path('my_cart/' ,my_cart),  #------
    path('logout/' ,logout),
    path('signup/' ,signup) ,
    



    path('term_and_condition/' , term_and_condition),
    
    path('privacy_policy/' , privacy_policy),
    path('return_policy/' , return_policy),
    path('contact_us/' , contact_us),
    path('career/' , career),
    path('team/',team),
   





    #-------reset password----------#
    path('password_reset/' ,PasswordResetView.as_view(template_name='home/password_reset_form.html') , name ='password_reset') ,
    path('password_reset/done/' ,PasswordResetDoneView.as_view(template_name='home/password_reset_done.html') , name ='password_reset_done') ,
    path('reset/<uidb64>/<token>/' ,PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html') , name ='password_reset_confirm') ,
    path('reset/done/' ,PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html') , name ='password_reset_complete') ,
    #-------reset password----------#


]
