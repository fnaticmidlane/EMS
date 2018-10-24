from django.db import models

from django.urls import reverse

# Create your models here.

class Registration (models.Model):

    class Meta:
        unique_together = (('event', 'participant'))

    event = models.ForeignKey(to = 'events.Event', on_delete = models.CASCADE)

    participant = models.ForeignKey(to = 'users.Participant', on_delete = models.CASCADE)

    parents_permit = models.FileField("Parent's Permit", upload_to = "uploads/permits/", default = '')
    parents_contact_number = models.CharField("Parent's Contact Number", max_length = 50)
    waiver = models.FileField("Waiver", upload_to = "uploads/waivers/", default = "")

    date_registered = models.DateTimeField("Date/Time Registered", auto_now_add = True)

    status = models.CharField("Status", max_length = 15, default = "Approved")

    def __str__(self):
        return "{}-{}".format(self.event, self.participant)

    def get_absolute_url(self):
        return reverse("registration_detail", kwargs ={"pk": self.pk})
        
