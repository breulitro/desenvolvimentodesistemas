from django.shortcuts import render
from .models import *


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
	return render(request, 'medical/pressure_sensor.html', {'patient': patient, 'value_high': '10', 'value_low': '5'})

###########################################################
