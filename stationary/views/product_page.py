from django.shortcuts import render

from stationary.models import StationaryStore
# Create your views here.




def show_stationary_product(request , slug):
   
    stationary=StationaryStore.objects.get(slug=slug)
    context={
        'stationary':stationary
    }
    return render(request , template_name="stationary/stationary_prduct_details.html" , context=context)
