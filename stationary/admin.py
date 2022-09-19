from django.contrib import admin

# Register your models here.

from stationary.models import Payment_st, StationaryImage, StationaryStore , Category , Publication_or_Brand , WritterName , IdealFor,Cart_st
# Register your order models here.


from stationary.models import Order_st,OrderItem_st,StationaryStore

from django.utils.html import format_html     #to create the link

# Register your models here.

class ImageItemConfiguration(admin.TabularInline):
    model = StationaryImage

class Cart_stConfiguration(admin.ModelAdmin):
    model = Cart_st
    list_display = ['quantity' , 'stationarystore' , 'user']

    fieldsets = (
        ("Cart_st Information", {"fields":('user', 'stationarystore' , 'quantity')}),
    )
    
class stationaryConfiguration(admin.ModelAdmin):
        model = StationaryStore
        list_display = ['get_image' , 'name' ,'discount' , 'price']
        list_editable = ['discount' ,'price']
        sortable_by = ['name']
        list_filter = ['category']
        list_display_links =['name']
        list_per_page = 12
        inlines=[ImageItemConfiguration]
        def get_image(self ,obj):
            return format_html(f"""
                <a target='_blank' href='{obj.image.url}'><img height='50px' src='{obj.image.url}'/></a>
            """)
        

class OrderItemConfiguration(admin.TabularInline):
    model = OrderItem_st

class OrderConfiguration(admin.ModelAdmin):
    model = Order_st
    list_display = ['user' , 'college' , 'phone' , 'date' , 'order_status']
    
    list_filter = ['order_status']
   # list_editable = ['order_status']
    fieldsets = (
    ("Order Information", {"fields":
    ('user' , 'college' ,'pincode', 'phone' , 'date','payment_method','total' , 'order_status', )}),

    ("Payment Information", {"fields":
    ('payment_st',
    'payment_request_id',
    'payment_id',
    'razorpay_signature',
    'payment_status',)}),
    )  
       
    readonly_fields = (
    'user' ,
    'college' ,
    'pincode',
   nt_request_id',
    'payment_id',
    'razorpay_signature',
    'payment_status',
    
    )  

    def payment_st(self , obj):
        payment_id = obj.payment_st_set.all()[0].id
        return format_html(f'<a href="/admin/home/payment/{payment_id}/change/" target="_blank">Click for  Payment Information</a>')

    def payment_request_id(self , obj):   
        return obj.payment_st_set.all()[0].payment_request_id 


    def payment_status(self , obj):   
        return obj.payment_st_set.all()[0].payment_status
    inlines = [OrderItemConfiguration]
     


#admin.site.register(Payment)
admin.site.register(Order_st ,OrderConfiguration )
admin.site.register(OrderItem_st)    
admin.site.register(Payment_st)




admin.site.register(StationaryStore , stationaryConfiguration)
admin.site.register(Category)
admin.site.register(Publication_or_Brand)
admin.site.register(WritterName)
admin.site.register(IdealFor)
admin.site.register(Cart_st , Cart_stConfiguration)
admin.site.register(StationaryImage)

