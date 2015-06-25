from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('medical.views',
	url(r'^$', index, name="index"),
	url(r'^access_log/$', access_log, name="access_log"),
	url(r'^sensors_list/(?P<patient_pk>\d+)$', sensors_list, name='sensors_list'),
	url(r'^blood_pressure_sensor/(?P<patient_pk>\d+)$', blood_pressure_sensor, name='blood_pressure_sensor'),
	url(r'^temperature_sensor/(?P<patient_pk>\d+)$', temperature_sensor, name='temperature_sensor'),
	url(r'^heartbeat_sensor/(?P<patient_pk>\d+)$', heartbeat_sensor, name='heartbeat_sensor'),
	url(r'^all_sensors/(?P<patient_pk>\d+)$', all_sensors, name='all_sensors'),
)
