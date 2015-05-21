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

	sensor_address = '127.0.0.1'
	sensor_port = 8888
	max_size = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sensor_address, sensor_port))
	s.send("get_pressure")
	data = s.recv(max_size)
	s.close()

	high = 0
	low = 0
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
