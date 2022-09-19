from django.http import request
from django.shortcuts import render ,redirect


from home.forms.checkout_form import Contact_us_form
from home.models import Contact_us 

def term_and_condition(request):
     return render(request , template_name='home/term_and_condition.html' )


def privacy_policy(request):
     return render(request , template_name='home/privacy_policy.html' )



def return_policy(request):
     return render(request , template_name='home/return_policy.html' )




def about_us(request):
     return render(request , template_name='home/about_us.html' )

def team(request):
     return render(request , template_name='home/team.html' )


def contact_us(request):
     if(request.method == 'GET'):
        form=Contact_us_form
        context={
           "form":form
        }
        return render(request , template_name='home/contact_us.html' , context=context)   
     
     else:
        form=Contact_us_form(request.POST)
        
        if(form.is_valid()):
            
            
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            subject=request.POST['subject']
            message=request.POST['message']

            contact_us=Contact_us()
            contact_us.name=name
            contact_us.message_status="pending"
            contact_us.email=email
            contact_us.phone=phone
            contact_us.subject=subject
            contact_us.message=message
            contact_us.save()

            

            
            
            return redirect('/contact_us')
        else:
            context={
              "form":form
            }
            return render(request , template_name='home/contact_us.html' , context=context)    


def career(request):
     return render(request , template_name='home/career.html' )