from django.shortcuts import render
from datetime import datetime

from .models import *

import json
import socket

SENSOR_IP = '127.0.0.1'
#SENSOR_IP = '169.254.164.81'
SENSOR_PORT = 8888

def index(request):
	access_log = AccessCounter()
	access_log.save()

	patients = Patient.objects.all()

	return render(request, 'medical/patient_list.html', {'patients': patients})

###########################################################
def access_log(request):
	date = datetime.now
	day = AccessCounter.objects.filter(date = date)
	month = AccessCounter.objects.filter(date = date)
	year = AccessCounter.objects.filter(date = date)

	return render(request, 'medical/access_log.html', {'day': len(day), 'month': len(month), 'year': len(year)})

###########################################################
def sensors_list(request, patient_pk):
	patient = Patient.objects.get(pk = patient_pk)
	address = Address.objects.get(patient = patient_pk)
	return render(request, 'medical/sensors_list.html', {'patient': patient, 'address': address})

###########################################################
def blood_pressure_sensor(request, patient_pk):
	patient = Patient.objects.get(pk = patient_pk)

	high = -1
	low = -1

	sensor_address = SENSOR_IP
	sensor_port = SENSOR_PORT
	max_size = 1024

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((sensor_address, sensor_port))
		s.send("get_pressure")
		data = s.recv(max_size)
		s.close()
	except:
		return render(request, 'medical/pressure_sensor.html', {'patient': patient, 'value_high': high, 'value_low': low})

	try:
		ret_val = json.loads(data)
		high = ret_val['value_high']
		low = ret_val['value_low']
	except:
		print "Data: %s" % data
		high = -1
		low = -1

	return render(request, 'medical/pressure_sensor.html', {'patient': patient, 'value_high': high, 'value_low': low})

###########################################################
def temperature_sensor(request, patient_pk):
	patient = Patient.objects.get(pk = patient_pk)

	value = -1

	sensor_address = SENSOR_IP
	sensor_port = SENSOR_PORT
	max_size = 1024

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((sensor_address, sensor_port))
		s.send("get_temperature")
		data = s.recv(max_size)
		s.close()
	except:
		return render(request, 'medical/temperature_sensor.html', {'patient': patient, 'value': value})

	try:
		ret_val = json.loads(data)
		value = ret_val['value']
	except:
		print "Data: %s" % data
		value = -1

	return render(request, 'medical/temperature_sensor.html', {'patient': patient, 'value': value})

###########################################################
def heartbeat_sensor(request, patient_pk):
	patient = Patient.objects.get(pk = patient_pk)

	value = -1

	sensor_address = SENSOR_IP
	sensor_port = SENSOR_PORT
	max_size = 1024

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((sensor_address, sensor_port))
		s.send("get_heartbeat")
		data = s.recv(max_size)
		s.close()
	except:
		return render(request, 'medical/heartbeat_sensor.html', {'patient': patient, 'value': value})

	try:
		ret_val = json.loads(data)
		value = ret_val['value']
	except:
		print "Data: %s" % data
		value = -1

	return render(request, 'medical/heartbeat_sensor.html', {'patient': patient, 'value': value})

###########################################################
def all_sensors(request, patient_pk):
	patient = Patient.objects.get(pk = patient_pk)

	heartbeat = -1
	temperature = -1
	high = -1
	low = -1

	sensor_address = SENSOR_IP
	sensor_port = SENSOR_PORT
	max_size = 1024

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((sensor_address, sensor_port))
		s.send("get_heartbeat")
		data1 = s.recv(max_size)

		s.send("get_temperature")
		data2 = s.recv(max_size)

		s.send("get_pressure")
		data3 = s.recv(max_size)

		s.close()
	except:
		return render(request, 'medical/all_sensors.html', {'patient': patient, 'temperature': temperature, 'heartbeat': heartbeat, 'value_high': high, 'value_low': low})

	try:
		ret_val = json.loads(data1)
		heartbeat = ret_val['value']
	except:
		heartbeat = -1

	try:
		ret_val = json.loads(data2)
		temperature = ret_val['value']
	except:
		temperature = -1

	try:
		ret_val = json.loads(data3)
		high = ret_val['value_high']
		low = ret_val['value_low']
	except:
		high = -1
		low = -1

	return render(request, 'medical/all_sensors.html', {'patient': patient, 'temperature': temperature, 'heartbeat': heartbeat, 'value_high': high, 'value_low': low})
