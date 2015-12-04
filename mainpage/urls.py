from . import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.user_login, name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^register/$', views.register, name='add-employee'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^invalid_login/$', views.InvalidDetails, name='invalid'),
	url(r'^personalinfo/$', views.EmployeeDetailView, name='personalinfo'),
]

