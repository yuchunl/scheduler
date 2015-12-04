from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse
from datetime import datetime
from contact.forms import UserProfileForm
from contact.models import UserProfile
from django.contrib.auth.models import User
import datetime
import pytz



@login_required
def index(request):
    user = request.user
    user_is_admin = False
    if (user.is_superuser|user.is_staff):
        user_is_admin = True
    contact_list = UserProfile.objects.all()
    context = {'contact_list':contact_list, 'user_is_admin':user_is_admin}
    #context = RequestContext(request)

    return render(request, 'contact/index.html', context)

@login_required
def detail(request, contact_id):
    userprofile = UserProfile.objects.get(pk=contact_id)
    #sth = UserProfile.objects.all()

    context = {'userprofile': userprofile}
    #context = RequestContext(request)
    return render(request, 'contact/detail.html', context)

@login_required
def edit(request, contact_id):
    # Like before, obtain the context for the user's request.
    new_user = UserProfile.objects.get(pk=contact_id)
    context = RequestContext(request)
    # If the request is a HTTP POST, try to pull out the relevant information.
    edited = False
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        new_user.title = request.POST['title']
        new_user.message = request.POST['message']
        new_user.save()
        edited = True
    return render_to_response('contact/edit.html',{'new_user': new_user, 'edited': edited}, context)



@login_required
def new(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    
    isprofiled = False
    user = str(request.user)
    #time = datetime.datetime.now()
    #today = datetime.date.today()
    #today = datetime.datetime.now()
    timePacific = datetime.datetime.now(pytz.timezone('US/Pacific-New'))
    time = timePacific.strftime("%Y-%m-%d %H:%M:%S")

    #userform = UserForm(data=request.POST)
    userprofileform = UserProfileForm(data=request.POST)
    #user = userprofileform.user
    #time = userprofileform.time
    # user1 = userprofileform.objects.create(user = '11111')
    # time1 = userprofileform.objects.create(time = time)

    # userprofileform.user = user1
    # userprofileform.time = time1

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        if userprofileform.is_valid():
            userprofile = userprofileform.save()
            userprofile.user = user
            userprofile.time = time
            userprofile.save()

            isprofiled = True

        #else:
            #print userprofileform.errors 


    else:

        userprofile = UserProfileForm()


    # Render the template depending on the context.
    return render_to_response(
            'contact/new.html',
            {'userprofileform': userprofileform, 'isprofiled': isprofiled, 'time' : time},
            context)




