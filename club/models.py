from django.db import models
from  django.contrib.auth.models import User

class Club(models.Model):
    Clubname = models.CharField(max_length=255)
    clubdescription=models.CharField(max_length=255)

    def __str__(self):
        return self.Clubname
    
    class Meta:
        db_table='Club'

class Meeting(models.Model):
    meetingTitle = models.CharField(max_length=255)
    meetingDate = models.DateField()
    meetingLocation = models.TextField()
    meetingTime=models.DurationField(null=True)
    meetingAgenda = models.TextField()

    def __str__(self):
        return self.meetingTitle
    
    class Meta:
        db_table='Meeting'
    
class Minutes(models.Model):
    # minutesmeeting=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    meetingId=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance = models.ManyToManyField(User)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    
    class Meta:
        db_table='Minutes'

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    meetingMinutes=models.ForeignKey(Minutes, on_delete=models.CASCADE)
    resourceType = models.CharField(max_length=255)
    dateEntered = models.DateTimeField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table='Resource'

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    eventResource=models.ForeignKey(Resource, on_delete=models.CASCADE)
    eventLocation = models.CharField(max_length=255)
    eventDate = models.DateTimeField()
    eventUserId = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    eventDesc = models.TextField()

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table='Event'