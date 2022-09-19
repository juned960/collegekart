
from email import message
from math import fabs
from re import I
from statistics import mode
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

    
  

class Extendeduser(models.Model):
    phone_num =models.CharField(max_length=15)
 
    college_name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)



class Contact_us(models.Model):
    message_status=(
        ('pending',"pending"),
        ('under_review',"under_review"),
        ('completed',"completed")
    )

    message_status=models.CharField(max_length=15,choices=message_status)
    name=models.CharField(max_length=25,null=False)
    email=models.EmailField(null=False)

    message=RichTextField(blank=True,null=False)
    date=models.DateTimeField(null=False , auto_now_add=True)

    def __str__(self):
        return str(self.email)