import time
import calendar
from datetime import date, datetime, timedelta

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, render
from django.core.context_processors import csrf
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import admin

from employee_schedule.models import *
from mainpage.models import *


mnames = "January February March April May June July August September October November December"
mnames = mnames.split()


def _show_users(request):
    """Return show_users setting; if it does not exist, initialize it."""
    s = request.session
    if not "show_users" in s:
        s["show_users"] = True
    return s["show_users"]

@login_required
def settings(request):
    """Settings screen."""
    s = request.session
    _show_users(request)
    if request.method == "POST":
        s["show_users"] = (True if "show_users" in request.POST else False)
    return render_to_response("manager_schedule/settings.html", add_csrf(request, show_users=s["show_users"]))

@login_required
def main(request):
    """Main listing, years and months; three years per page."""
    year = date.today().year
    month = date.today().month
    return render_to_response("manager_schedule/main.html", dict(year=year, month=month))
 
@login_required
def month(request, year=None, month=None, change=None):
    """Listing of days in `month`."""
    if year is None:
        year = date.today().year
    
    if month is None:
        month = date.today().month
    year, month = int(year), int(month)

    # apply next / previous change
    if change in ("next", "prev"):
        now, mdelta = date(year, month, 15), timedelta(days=31)
        if change == "next":   mod = mdelta
        elif change == "prev": mod = -mdelta

        year, month = (now+mod).timetuple()[:2]

    # init variables
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    nyear, nmonth, nday = time.localtime()[:3]
    lst = [[]]
    week = 0

    # make month lists containing list of days for each week
    # each day tuple will contain list of entries and 'current' indicator
    for day in month_days:
        entries = current = False   # are there entries for this day; current day?
        if day:
            if not _show_users(request):
                entries = entries.filter(creator=request.user)
            if day == nday and year == nyear and month == nmonth:
                current = True

        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    return render_to_response("manager_schedule/month.html", dict(year=year, month=month, user=request.user,
                        month_days=lst, mname=mnames[month-1]))

@login_required
def day(request, year, month, day):
    # availtime_queryset = timeslot records on selected day
    timeslot_queryset = TimeSlot.objects.filter(date=date(int(year),int(month),int(day)), if_assigned=False).exclude(creator=None)
    return render_to_response('manager_schedule/day.html', dict(year=year, month=month, day=day, timeslot_list=timeslot_queryset), context_instance=RequestContext(request))
    
@login_required
def select_time(request):
    if request.method == 'POST':
        #print request.POST.getlist('timeslot')
        assigned_time_lst = request.POST.getlist('timeslot')
        for assigned_time in assigned_time_lst:
            approved_time = TimeSlot.objects.get(pk=assigned_time)
            #print approved_time.if_assigned
            approved_time.if_assigned = True
            approved_time.save()
            #print approved_time.if_assigned
        
    return render_to_response('manager_schedule/a_template.html',{day:day})

@login_required
def assigned_time(request):
    assigned_time_list = TimeSlot.objects.filter(if_assigned=True)
    distinct_date = TimeSlot.objects.filter(if_assigned=True).order_by().values('date').distinct()
    #print distinct_date
    #print assigned_time_list
    return render_to_response("manager_schedule/view_schedule.html", dict(assigned_time_list=assigned_time_list, distinct_date=distinct_date))
    #return render_to_response("manager_schedule/view_schedule.html", dict(distinct_date=distinct_date))


@login_required
def get_closed_days(request, year=None, month=None, change=None):    
    """
    sub_timeslot_list = TimeSlot.objects.filter(start='09:00'); 
    if request.method == 'POST':
        print request.POST.getlist('open_days_list')
        open_days_list = request.POST.getlist('open_days_list')
        for open_day in open_days_list:
            approved_time = TimeSlot.objects.get(pk=open_day)
            print approved_time.is_open
            approved_time.is_open = True
            approved_time.save()
            print approved_time.is_open
    """
    if year is None:
        year = date.today().year
    
    if month is None:
        month = date.today().month
    year, month = int(year), int(month)

    # apply next / previous change
    
    if change in ("next", "prev"):
        now, mdelta = date(year, month, 15), timedelta(days=31)
        if change == "next":   mod = mdelta
        elif change == "prev": mod = -mdelta

        year, month = (now+mod).timetuple()[:2]
    
    
    # init variables
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    nyear, nmonth, nday = time.localtime()[:3]
    lst = [[]]
    week = 0

    for day in month_days:
        entries = current = False   # are there entries for this day; current day?
        if day:
            if not _show_users(request):
                entries = entries.filter(creator=request.user)
            if day == nday and year == nyear and month == nmonth:
                current = True

        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    #return render_to_response("manager_schedule/month.html", dict(year=year, month=month, user=request.user,
    #                    month_days=lst, mname=mnames[month-1]))
        
    date_list = TimeSlot.objects.order_by().values('date').distinct()
    
    return render_to_response('manager_schedule/open_day.html',dict(year=year, month=month, user=request.user,
                        month_days=lst, mname=mnames[month-1], date_list=date_list), context_instance=RequestContext(request))
    

@login_required
def open_day(request):  

    if request.method == 'POST':
        #print request.POST.getlist('closed_day')
        dkey_list = request.POST.getlist('closed_day')
        
        for dkey in dkey_list:
            d = date(int(dkey[0:4]), int(dkey[4:6]), int(dkey[6:8]))
            #print d
            
            a1_pk = int(dkey) + 1
            a1 = TimeSlot(a1_pk, None, d, "09:00:00", "12:00:00")
            a1.save()
            a2_pk = int(dkey) + 2
            a2 = TimeSlot(a2_pk, None, d, "14:00:00", "17:00:00")
            a2.save()
            a3_pk = int(dkey) + 3
            a2 = TimeSlot(a3_pk, None, d, "18:00:00", "21:00:00")
            a2.save()
            
    return render_to_response('manager_schedule/a_template.html', context_instance=RequestContext(request))

def add_csrf(request, **kwargs):
    """Add CSRF and user to dictionary."""
    d = dict(user=request.user, **kwargs)
    d.update(csrf(request))
    return d

@login_required
def view_employees(request):


    group = UserProfile.objects.all()
    username = request.POST.get('username')

    for employee in group:
        if employee.user == username:
            phone_num = employee.phone_num
            address = employee.address

    return render_to_response("manager_schedule/view_employees.html", dict(group=group), context_instance = RequestContext(request))


    #return render_to_response("manager_schedule/view_employees.html", dict(group=group), context_instance=RequestContext(request))



