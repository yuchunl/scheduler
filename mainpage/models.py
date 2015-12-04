from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    #username = models.ForeignKey(User, blank = True, null = True)
    user = models.OneToOneField(User)
    phone_num = models.CharField(max_length = 12)
    address = models.CharField(max_length = 255)

    GENDER_CHOICES = (
    	('male', 'Male'),
    	('female', 'Female'),
		)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
    	return self.user.username




		



	
