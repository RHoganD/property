from django.shortcuts import render, get_object_or_404
from django.views import  generic, View
from .models import Property,  Category



# Create your views here.
def property_list(request):
    property_list = Property.objects.all()
    template = 'app/property_list.html'
    context = {

         'property_list' : property_list
    }
    paginate_by = 6
    
    return render(request, template, context)
    

def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'app/property_detail.html'
    context = {
        'property_detail' : property_detail
    }

    return render(request, template, context)



def home(generic):
    home =  Property.objects.all()
    template = 'app/index.html' 
    context = {
        'index.html' : home
    }
    return render(generic, template, context)