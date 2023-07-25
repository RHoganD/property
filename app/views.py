from django.shortcuts import render, get_object_or_404
from django.views import  View
from .models import Property,  Category



# Create your views here.
def property_list(request):
    property_list = Property.objects.all()
    template = 'agency/property_list.html'
    context = {

         'property_list' : property_list
    }
    paginate_by = 6
    
    return render(request, template, context)
    

def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'agency/property_detail.html'
    context = {
        'property_detail' : property_detail
    }

    return render(request, template, context) 


def home(request):
    home =  Property.objects.all()
    template = 'agency/index.html' 
    context = {
        'index.html' : home
    }
    return render(request, template, context)