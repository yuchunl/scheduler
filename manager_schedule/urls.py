from django.conf.urls import patterns, url, include
#from dbe.cal.models import *
#from todo.models import *
from . import views

urlpatterns = [

    url(r'^month/(\d+)/(\d+)/(prev|next)/$', views.month),
    url(r'^month/(\d+)/(\d+)/$', views.month),
    url(r'^month$', views.month),
    url(r'^assigned_time/$', views.assigned_time),
    url(r'^day/(\d+)/(\d+)/(\d+)/$', views.day),
    url(r'^settings/$', views.settings),
    url(r'^(\d+)/$', views.main),
    url(r'^select_time/$',views.select_time),
    url(r'^get_closed_days/(\d+)/(\d+)/(prev|next)/$$',views.get_closed_days),
    url(r'^get_closed_days/(\d+)/(\d+)/$', views.get_closed_days),
    url(r'^get_closed_days', views.get_closed_days),
    url(r'^open_day/$',views.open_day),
    url(r'^$', views.main, name='manager-main'),
    url(r'employee_list/$', views.view_employees, name = 'view-employees'),
    #url(r'^$', views.main),
]
