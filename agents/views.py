from django.shortcuts import render
from django.views import  View
from .models import Agent


# Create your views here.
def agent_list(request):
    agent_list = Agent.objects.last()
    template = 'agents/agents.html' 
    context = {
        'agent_list' : agent_list
    }
    return render(request, template, context)
