from random import choices
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User 



#>>>>--------------Customerloginform---start---------------#

class CustomerloginForm(AuthenticationForm):
    username=forms.EmailField(required=True , label="Email" )


college_name=(
        ('Budge Budge Institute of Technology kokata',"Budge Budge Institute of Technology kokata"),
        ('Jagannath Gupta Institue of Medical Science and Hospital',"Jagannath Gupta Institue of Medical Science and Hospital"),
    )
#--------------Customerloginform---end---------------<<<<#



#>>>>--------------CustomerCreationform---start---------------#

class CustomerCreationForm(UserCreationForm):
    username=forms.EmailField(required=True , label="Email" )
    first_name=forms.CharField(required=True , label="First Name" )
    last_name=forms.CharField(required=True , label="Last Name" )
    college_name=forms.ChoiceField(required=True , label="College Name" , choices=college_name)
    phone_number=forms.IntegerField( label="Phone Number")
    pincode=forms.IntegerField(label="Pincode")

    class Meta:
        model= User
        fields = ['username' , 'first_name' , 'last_name' ,'college_name','pincode','phone_number']

#--------------CustomerCreationform---end---------------<<<<#




    