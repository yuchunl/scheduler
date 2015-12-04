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

from django.contrib.auth.models import User
from django.contrib import admin

from .models import *


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
    return render_to_response("employee_schedule/settings.html", add_csrf(request, show_users=s["show_users"]))

@login_required
def main(request):
    """Main listing, years and months; three years per page."""
    year = date.today().year
    month = date.today().month
    return render_to_response("employee_schedule/main.html", dict(year=year, month=month))


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
            #entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
            if not _show_users(request):
                entries = entries.filter(creator=request.user)
            if day == nday and year == nyear and month == nmonth:
                current = True

        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    open_date_lst = TimeSlot.objects.order_by().values('date').distinct()
    return render_to_response("employee_schedule/month.html", dict(year=year, month=month, user=request.user,
                        month_days=lst, mname=mnames[month-1], open_date_lst=open_date_lst))

@login_required
def day(request, year, month, day):
    # availtime_queryset = timeslot records on selected day
    availtime_queryset = TimeSlot.objects.filter(date=date(int(year),int(month),int(day)), creator=None)
    return render_to_response('employee_schedule/day.html', dict(year=year, month=month, day=day, avail_time=availtime_queryset), context_instance=RequestContext(request))
    
def select_time(request):
    if request.method == 'POST':
        selected_timeslot = TimeSlot.objects.get(pk=request.POST['availtime'])
        #print request.POST['availtime']
        #print selected_timeslot.creator
        selected_timeslot.creator_id = request.user
        selected_timeslot.save()
        #print selected_timeslot.creator
        return render_to_response('employee_schedule/a_template.html', request)

def view_schedule(request):
    availibility_list = TimeSlot.objects.filter(creator_id=request.user)
    #print availibility_list
    return render_to_response("employee_schedule/view_schedule.html", dict(availibility_list=availibility_list))

def add_csrf(request, **kwargs):
    """Add CSRF and user to dictionary."""
    d = dict(user=request.user, **kwargs)
    d.update(csrf(request))
    return d
