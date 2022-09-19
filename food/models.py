from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.



#----------------------------







# Create your models here.


class Foodproperty(models.Model):
    title=models.CharField(max_length=60 ,null=False)
    slug=models.CharField(max_length=60 , null=False , unique=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
    

class Category(Foodproperty):
    pass

class FoodStore(models.Model):
    name=models.CharField(max_length=80 , null=False)
    sub_name=models.CharField(max_length=15,null=False)
    slug=models.CharField(max_length=150 , null=True , unique=True , default="" )
    description=RichTextField(blank=True,null=True)
    image=models.ImageField(upload_to='upload/images' , null=False)
    price=models.IntegerField(default=0 , null=True)
    discount=models.IntegerField(default=0)
    category=models.ForeignKey(Category , on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    
class FoodImage(models.Model):
    foodstore = models.ForeignKey(FoodStore , on_delete=models.CASCADE)
    foodimg =models.ImageField(upload_to='upload/images',null=False)


    def __str__(self):
        return self.foodstore.name


  
class Order_fd(models.Model):
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
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
  
class OrderItem_fd(models.Model):
    order= models.ForeignKey(Order_fd, on_delete=models.CASCADE)
    foodstore= models.ForeignKey(FoodStore, on_delete=models.CASCADE)
   

  
class Payment(models.Model):
    order= models.ForeignKey(Order_fd, on_delete=models.CASCADE)
    date=models.DateTimeField(null=False , auto_now_add=True)

    razorpay_signature= models.CharField(max_length=200 ,null=False)

    def __str__(self):
        return self.payment_id

#------------------------




class Carousel(models.Model):
    name=models.CharField(max_length=60 ,null=False)
    image=models.ImageField(upload_to='upload/images' , null=False)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    foodStore=models.ForeignKey(FoodStore , on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE )
    quantity=models.IntegerField(default=1)