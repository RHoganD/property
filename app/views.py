from django.shortcuts import render
from django.views import  generic, View
from .models import Property , Category
from .forms import ViewingForm



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


    if request.method == 'Post':
        viewing_form = ViewingForm(request.POST)
        if viewing_form.is_valid():
            viewing_form.save()
            return redirect('property_list')
    
    else:
        viewing_form = ViewingForm()

    context = {
        'property_detail' : property_detail,
        'viewing_form' : viewing_form
    }

    return render(request, template, context)



def home(generic):
    home =  Property.objects.all()
    template = 'app/index.html' 
    context = {
        'index.html' : home
    }
    return render(generic, template, context)


def about(generic):
    about =  Property.objects.all()
    template = 'app/about.html' 
    context = {
        'about.html' : about
    }
    return render(generic, template, context)