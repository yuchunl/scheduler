from django.db import models 
import datetime

# Create your models here.

#from django.contrib.auth.models import User



class UserProfile(models.Model):
	
	user = models.CharField(max_length=200, null=True, blank=True)
	#user = models.OneToOneField(User)
	title = models.CharField(max_length=80, null=False, blank=False)
	message = models.CharField(max_length=200, null=True, blank=True)
	time = datetime.datetime.now()
	time = models.CharField(max_length=200, null=True, blank=True)
