from collections import UserList
from django.shortcuts import render
from .models import Club, Meeting, Event, Resource, Minutes

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def members(request):
    user_list = Resource.objects.all()
    return render(request, 'club/members.html', {'user_list': user_list})

