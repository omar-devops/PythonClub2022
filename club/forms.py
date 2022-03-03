from itertools import product
from django import forms
from .models import Club, Meeting, Event, Resource, Minutes

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='_all_'
