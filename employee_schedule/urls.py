from django.conf.urls import patterns, url, include
from . import views

urlpatterns = [
    url(r"^month/(\d+)/(\d+)/(prev|next)/$", views.month ),
    url(r"^month/(\d+)/(\d+)/$", views.month),
    url(r"^month$", views.month),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", views.day),
    url(r"^settings/$", views.settings),
    url(r"^select_time/$",views.select_time),
    url(r"^view_schedule/$",views.view_schedule, name = "view-schedule"),
    url(r"^$", views.main, name = 'employee-main'),
 ]