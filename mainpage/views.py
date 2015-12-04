from django.shortcuts import render, render_to_response
from django.views.generic import DetailView
from mainpage.forms import UserForm, UserProfileForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext

from datetime import date, datetime, timedelta

@login_required
def register(request):
	context = RequestContext(request)

	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			#save User object
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			registered = True
		else:
			print (user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
			'add_employee.html',
			{'user_form':user_form, 'profile_form': profile_form,'registered': registered}, context)

def user_login(request):

	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		employee = False

		employee = authenticate(username = username, password = password)
		
		if employee is not None:
			if (employee.is_superuser|employee.is_staff):
				if employee.is_active:
					login(request, employee)
					#print "im admin"
					return render_to_response('manager_schedule/main.html', dict(year=date.today().year, month=date.today().month, username=username))
			elif employee:
				if employee.is_active:
					login(request, employee)
					return render_to_response('employee_schedule/main.html', dict(year=date.today().year, month=date.today().month, username=username))
				else:
					return HttpResponse("Your account is disabled.")
		else:
			return render(request, 'invalid_login.html')
	else:
		return render_to_response('login.html', {}, context)

def user_logout(request):

	logout(request)

	return HttpResponseRedirect('/Scheduler/')


@login_required
def index(request):
	c = {}
	c.update(csrf(request))
	username = request.user
	if username.is_superuser:
		#return render(request, 'LandingPage.html', {})
		return render_to_response('manager_schedule/main.html', dict(year=date.today().year, month=date.today().month, username=username))
	else:
		return render_to_response('employee_schedule/main.html', dict(year=date.today().year, month=date.today().month, username=username))

@login_required
def EmployeeDetailView(request):
	#user = django.contrib.auth.get_user_model()
	user = request.user
	#employeeName = u.employee.username
	#employeeModel = Employee.objects.get(address=user.employee.address )
	#context = {'employee_info':
	return render(request, 'personal_info.html')

def InvalidDetails(request):
	return render(request, 'invalid_details.html')
	
	
	
