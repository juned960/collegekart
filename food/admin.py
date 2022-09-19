from django.contrib import admin
from food.models import FoodStore , Category ,Cart , Carousel, FoodImage
from django.utils.html import format_html  



from food.models import Payment , Order_fd , OrderItem_fd 
from django.utils.html import format_html    
# Register your models here.

class CartConfiguration(admin.ModelAdmin):
    model = Cart
    list_display = ['quantity' , 'foodStore' , 'user']

    fieldsets = (
        ("Cart Information", {"fields":('user', 'foodStore' , 'quantity')}),
    )
    
  
class ImageItemConfiguration(admin.TabularInline):
    model = FoodImage


class FoodConfiguration(admin.ModelAdmin):
    model = FoodStore
    list_display = ['get_image' , 'name' ,'discount' , 'price']
    list_editable = ['discount' ,'price']
    sortable_by = ['name']
    list_filter = ['category']
    
    list_per_page = 12
    inlines=[ImageItemConfiguration]
    def get_image(self ,obj):
        return format_html(f"""
             <a target='_blank' href='{obj.image.url}'><img height='50px' src='{obj.image.url}'/></a>
        """)
    


    

#------------------------->
class OrderItemConfiguration(admin.TabularInline):
    model = OrderItem_fd

class OrderConfiguration(admin.ModelAdmin):
    model = Order_fd
    list_display = ['user' , 'college' , 'phone' , 'date' , 'order_status']
    
    list_filter = ['order_status']
   # list_editable = ['order_status']
    fieldsets = (
    ("Order Information", {"fields":
    ('user' , 'college' ,'pincode', 'phone' , 'date','payment_method','total' , 'order_status', )}),

    ("Payment Information", {"fields":
    ('payment',
    'payment_request_id',
    'payment_id', 
    'razorpay_signature',
    'payment_status',)}),
    )  
    
       
    readonly_fields = (
    'user' ,
    'payment_method' ,
    'payment',
    'payment_request_id',
    'payment_id',
    'razorpay_signature',
    'payment_status',
    
    )  

    def payment(self , obj):
        payment_id = obj.payment_set.all()[0].id
        return format_html(f'<a href="/admin/home/payment/{payment_id}/change/" target="_blank">Click for  Payment Information</a>')

    def payment_request_id(self , obj):   
        return obj.payment_set.all()[0].payment_request_id 

    def razorpay_signature(self , obj):   
        return obj.payment_set.all()[0].razorpay_signature     


    def payment_id(self , obj):   
        payment_id = obj.payment_set.all()[0].payment_id  
        if (payment_id is None or payment_id ==''):
            return "Payment Id is not  Available"
        else:
            return  payment_id

    def payment_status(self , obj):   
        return obj.payment_set.all()[0].payment_status
    inlines = [OrderItemConfiguration]
     

#--------------------->









admin.site.register(FoodStore , FoodConfiguration)
admin.site.register(Category)
admin.site.register(Carousel)




admin.site.register(Payment)

admin.site.register(Order_fd ,OrderConfiguration )
admin.site.register(OrderItem_fd) 
admin.site.register(FoodImage)
