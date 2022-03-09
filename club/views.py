from collections import UserList
from django.shortcuts import get_object_or_404, render
from .models import Club, Meeting, Event, Resource, Minutes
from django.urls import reverse_lazy
from .forms import EventForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def members(request):
    user_list = Resource.objects.all()
    return render(request, 'club/members.html', {'user_list': user_list})
  
def meetings(request, id):
    eventResource = get_object_or_404(Event, pk=id)
    return render(request, 'club/meetings.html', {'eventResource': eventResource})

@login_required
def newEvent(request):
    form=EventForm

    if request.method == 'POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
        
    else:
        form=EventForm()
    return render(request,'club/newevent.html', {'form': form})

def  loginmessage(request):
        return render(request, 'club/loginmessage.html')
    
def  logoutmessage(request):
        return render(request, 'club/logoutmessage.html')