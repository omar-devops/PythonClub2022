from collections import UserList
from django.shortcuts import render
from .models import Meeting, Event, Resource, Minutes

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def members(request):
    user_list = Event.objects.all()
    return render(request, 'club/members.html', {'user_list': user_list})

