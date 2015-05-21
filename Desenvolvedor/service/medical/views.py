from django.shortcuts import render
from .models import *

import json
import socket


def index(request):
	patients = Patient.objects.all()

	return render(request, 'medical/patient_list.html', {'patients': patients})

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

	sensor_address = '127.0.0.1'
	sensor_port = 8888
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

	sensor_address = '127.0.0.1'
	sensor_port = 8888
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
