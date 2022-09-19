from django.contrib import admin
from home.models import Extendeduser ,Contact_us
from home.views.footer import contact_us

 

# Register your models here.
class Contact_usConfiguration(admin.ModelAdmin):
    model = Contact_us
    list_display = ['email','name' ,'message_status' ]
    sortable_by = ['date']
    list_filter = ['message_status']
   


admin.site.register(Extendeduser)
admin.site.register(Contact_us, Contact_usConfiguration)


