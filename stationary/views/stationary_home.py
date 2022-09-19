from django.shortcuts import render

from stationary.models import StationaryStore , Category


from django.core.paginator import Paginator

from urllib.parse import urlencode
# Create your views here.

"""
def sthome(request):
    stationarystorte=StationaryStore.objects.all()
    for i in stationarystorte:
     print(i)
    context ={
        "stationarystore": stationarystorte
    } 
    return render(request , template_name='stationary/sthome.html',context = context)


"""



def sthome(request):
    query=request.GET
    stationarystore = []
    stationarystore=StationaryStore.objects
    
    categorys = query.get('category')
    page = query.get('page')
    if(page is  None or page == ''):
        page = 1

    
  



    category=Category.objects.all()

    

    paginator = Paginator(stationarystore ,8)
    page_object = paginator.get_page(page)

    query = request.GET.copy()
    query['page'] = ''
    pageurl = urlencode(query)
    print(urlencode(query) , " query")

    context={
        'page_object':page_object,                #'stationarystore':stationarystore
        'category':category,
        'pageurl':pageurl,
    }
    return render(request , template_name='stationary/sthome.html' , context=context)



def show_stationary_product(request , slug):
   
    stationary=StationaryStore.objects.get(slug=slug)
    context={
        'stationary':stationary
    }
    return render(request , template_name="stationary/stationary_prduct_details.html" , context=context)
