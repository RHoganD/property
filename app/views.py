from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Property, Category, About
from .forms import ViewingForm
from django.db.models import Q



def property_list(request):
    property_list = Property.objects.all()
    template = 'app/property_list.html'

    address_query = request.GET.get('q')
    property_type = request.GET.getlist('property_type', None)
    if address_query and property_type :
        property_list = property_list.filter(
            Q(name__icontains = address_query) &
            Q(property_type__icontains=property_type[0])
        ).distinct()

        print(property_list)   

    context = {

         'property_list' : property_list
    }
    paginate_by = 6
    
    return render(request, template, context)
    

def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'app/property_detail.html'


    if request.method == 'Post':
        viewing_form = ViewingForm(request.POST)
        if viewing_form.is_valid():
            viewing_form.save()
            return HttpResponseRedirect(reverse('property_list'))
           
    
    else:
        viewing_form = ViewingForm()

    context = {
        'property_detail' : property_detail,
        'viewing_form' : viewing_form
    }

    return render(request, template, context)



def about(request):
    about = About.objects.all()
    template = 'app/about.html'
    context = {
        'about.html' : about 
    }

    return render(request, template, context)