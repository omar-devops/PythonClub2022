# from django.contrib import admin
# from .models import Meeting
# # , Minutes, Resource, Event

# # Register your models here.
# admin.site.register('Meeting')
# # # admin.site.register('Minutes')
# # # admin.site.register('Resource')
# # # admin.site.register('Event')

from django.contrib import admin
from .models import Club, Meeting, Minutes, Resource, Event
# Register your models here.
# Necessary if they are to appear in the admin
admin.site.register(Club)
admin.site.register(Meeting)
admin.site.register(Minutes)
admin.site.register(Resource)
admin.site.register(Event)


