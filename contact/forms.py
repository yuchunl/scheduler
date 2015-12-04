from contact.models import UserProfile
from django.contrib.auth.models import User
from django import forms


#class UserForm(forms.ModelForm):
	
	#class Meta:
		#model = User
		#fields = ('first_name', 'last_name', 'email','confirm_password')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('title', 'message','user','time')

		exclude = ('user','time')
