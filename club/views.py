from collections import UserList
from django.shortcuts import get_object_or_404, render
from .models import Club, Meeting, Event, Resource, Minutes
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def members(request):
    user_list = Resource.objects.all()
    return render(request, 'club/members.html', {'user_list': user_list})

def meetings(request, id):
    meeting = get_object_or_404(Event, pk=id)
    return render(request, 'club/meetings.html', {'meeting': meeting})

