from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    name = models.CharField("Name of Event", max_length = 50)
    description = models.TextField("Description", max_length = 1000, blank = True)

    max_slots = models.IntegerField("Max Slots", blank = True, null = True)
    date_from = models.DateField("Start Date", null = True)
    date_to = models.DateField("End Date", null = True)
    time_from = models.TimeField("Start Time", null = True)
    time_to = models.TimeField("End Time", null = True)

    venue = models.CharField("Venue", max_length = 200, default = '')

    creator = models.ForeignKey(to = 'users.Participant', on_delete = models.CASCADE, null = True)


    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs = {"pk": self.pk})