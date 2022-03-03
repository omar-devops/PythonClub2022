from django.test import TestCase
from .models import Club, Meeting, Event, Resource, Minutes
from  .forms import EventForm
from django.contrib.auth.models import User
from pythonclub2022.club.forms import EventForm
import datetime
from django.urls import revers

# Create your tests here.
class ClubTest(TestCase):
    def setUp(self):
        self.type=Club(Clubname='C#')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'C#')

    def test_tablename(self):
        self.assertEqual(str(Club._meta.db_table), 'Club')        

class EventTest(TestCase):
    def setUp(self):
            self.type=Club(Clubname='C#')
            self.user = User(username="user1")
            self.event = Event(eventTitle = 'C#', eventUserId = self.user, eventDesc='C# Training', eventDate='02/22/2022', eventLocation='Bellevue')

    def test_string(self):
            self.assertEqual(str(self.event), 'C#')
    
    def test_certificate(self):
        cert = self.event.eventTitle
        self.assertEqual(self.event.certificate(), cert)
    
class NewEventForm(TestCase):
    def test_eventform_is_valid(self):
        data = {
            {'eventtitle':'python', 'eventResource': 'python club', 'eventUserId': 'omurbek', 'eventDate':'2022-3-1', 'eventLocation': 'Seattle', 'eventDesc': 'Intro to python'}
            } 
        form=EventForm(data)
        self.assertTrue(form.is_valid())
    def test_Eventform_invalid(self):
         data = {
            {'eventtitle':'python', 'eventResource': 'python club', 'eventUserId': 'omurbek', 'eventDate':'2022-3-1', 'eventLocation': 'Seattle', 'eventDesc': 'Intro to python'}
            } 
        form=EventForm(data)
        self.assertFalse(form.is_valid())
        