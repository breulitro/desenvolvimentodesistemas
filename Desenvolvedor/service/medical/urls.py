from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('medical.views',
	url(r'^$', index, name="index"),
	url(r'^sensors_list/(?P<patient_pk>\d+)$', sensors_list, name='sensors_list'),
	url(r'^blood_pressure_sensor/(?P<patient_pk>\d+)$', blood_pressure_sensor, name='blood_pressure_sensor'),

#	url(r'^guest_create$', GuestCreate.as_view(), name="guest_create"),
#	url(r'^guest_list$', GuestList.as_view(), name="guest_list"),
#	url(r'^guest_update/(?P<pk>\d+)/$', GuestUpdate.as_view(), name="guest_update"),
#	url(r'^guest_delete/(?P<pk>\d+)/$', GuestDelete.as_view(), name="guest_delete"),
)
