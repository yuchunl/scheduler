from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
#from login.models import SignUp


class TimeSlot(models.Model):
    creator = models.ForeignKey(User, blank=True, null=True)
    date = models.DateField(blank=True)
    start = models.TimeField(("start"))
    end = models.TimeField(("end"))
    if_assigned = models.BooleanField(default=False)
    is_open = models.BooleanField(default=False)
    #availability = models.BooleanField(default=True)
    def __str__(self):
        return str(self.date) + ' ' +str(self.start) +' '+ str(self.end)
  
  
### Admin

class EntryAdmin(admin.ModelAdmin):
    list_display = ["creator", "date", "title", "snippet"]
    search_fields = ["title", "snippet"]
    list_filter = ["creator"]
