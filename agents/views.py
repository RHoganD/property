from django.shortcuts import render, get_object_or_404
from django.views import  View
from .models import Agent


# Create your views here.
def agent_list(request):
    agent_list = Agent.objects.all()
    template = 'app/agents.html' 
    context = {
        'agents.html' : agent_list
    }
    return render(request, template, context)
