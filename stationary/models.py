from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField


# Create your models here.

class Stationaryproperty(models.Model):
    title=models.CharField(max_length=60 ,null=False)
    slug=models.CharField(max_length=60 , null=False , unique=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
    

class Category(Stationaryproperty):
    pass

class Publication_or_Brand(Stationaryproperty):
    pass

class WritterName(Stationaryproperty):
    pass

class IdealFor(Stationaryproperty):
    pass



    
                
class StationaryStore(models.Model):
    category=models.ForeignKey(Category , on_delete=models.CASCADE)
    name=models.CharField(max_length=80 , null=False)
    sub
    idealfor=models.ForeignKey(IdealFor , on_delete=models.CASCADE)
    description=RichTextField(blank=True,null=True)
    image=models.ImageField(upload_to='upload/images' , null=False)
    price=models.IntegerField(default=0 , null=True)
    discount=models.IntegerField(default=0)
    

    
    def __str__(self):
        return self.name




class StationaryImage(models.Model):
    stationarystore = models.ForeignKey(StationaryStore , on_delete=models.CASCADE)
    stationaryimg =models.ImageField(upload_to='upload/images',null=False)


    def __str__(self):
        return self.stationarystore.name


class Cart_st(models.Model):
    stationarystore=models.ForeignKey(StationaryStore , on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE )
    quantity=models.IntegerField(default=1)



# Create your order models here.

    
  
class Order_st(models.Model):
    orderStatus=(
        ('PENDING',"pending"),
        ('PLACED',"placed"),
        ('CANCELED',"canceled"),
        ('COMPLETED',"completed"),
    )
    method=(
        ('COD',"Cash on Delivery"),
        ('ONLINE',"Pay Online"),
       
    )
    college_name=(
        ('Budge Budge Institute of Technology kokata',"Budge Budge Institute of Technology kokata"),
        ('Jagannath Gupta Institue of Medical Science and Hospital',"Jagannath Gupta Institue of Medical Science and Hospital"),
    )
   
    order_status= models.CharField(max_length=15 , choices=orderStatus)
    payment_method= models.CharField(max_length=20 ,default='Cash on Delivery', choices=method)
    college= models.CharField(max_length=60 , choices=college_name , null=False)
    
    pincode= models.IntegerField( null=False)
    phone = models.CharField(max_length=102 , null=False)
  
    date=models.DateTimeField(null=False , auto_now_add=True)
    
  
class OrderItem_st(models.Model):
    order= models.ForeignKey(Order_st, on_delete=models.CASCADE)
    stationarystore= models.ForeignKey(StationaryStore, on_delete=models.CASCADE)
    quantity=models.IntegerField( null=False)
    price=models.IntegerField( null=False)
    date=models.DateTimeField(null=False , auto_now_add=True)



class Payment_st(models.Model):
    order= models.ForeignKey(Order_st, on_delete=models.CASCADE)
    date=models.DateTimeField(null=False , auto_now_add=True)
 
    payment_request_id= models.CharField(max_length=200 ,null=False)
    razorpay_signature= models.CharField(max_length=200 ,null=False)




    def __str__(self):
        return self.payment_id



  

    
    