from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('medical.views',
	url(r'^$', index, name="index"),
	url(r'^sensors_list/(?P<patient_pk>\d+)$', sensors_list, name='sensors_list'),
	url(r'^blood_pressure_sensor/(?P<patient_pk>\d+)$', blood_pressure_sensor, name='blood_pressure_sensor'),
	url(r'^temperature_sensor/(?P<patient_pk>\d+)$', temperature_sensor, name='temperature_sensor'),
)
