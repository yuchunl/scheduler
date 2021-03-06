from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='message-index'), # ADD NEW PATTERN!
    url(r'^new/$', views.new, name='message-new'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.detail, name='message-detail'),
    url(r'^(?P<contact_id>[0-9]+)/edit/$', views.edit, name='message-edit'),

]
