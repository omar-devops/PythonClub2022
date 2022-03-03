from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('meetings/<int:id>', views.meetings, name = 'meetings'),
    path('newEvent/', views.newEvent, name='newevent'),
]