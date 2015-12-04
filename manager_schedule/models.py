from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
#from login.models import SignUp


"""
class AssignedTime(models.Model):
    creator = models.ForeignKey(User, blank=True, null=True)
    date = models.DateField(blank=True)
    start = models.DateTimeField(("start"))
    end = models.DateTimeField(("end"), help_text=("The end time must be later than the start time."))
    #availability = models.BooleanField(default=True)
    def __str__(self):
        return str(self.date) + ' ' +str(self.start) +' '+ str(self.end)
"""
 