# -*- coding: utf-8 -*-

from django.db import models

GENDERCHOICE = (
	('M', 'Male'),
	('F', 'Female'),
)

class Patient(models.Model):
	email = models.EmailField(max_length=80, unique=True)
	name = models.CharField(max_length=80)
	lastname = models.CharField(max_length=80)
	occupation = models.CharField(max_length=200);
	gender = models.CharField(max_length=1, choices=GENDERCHOICE)
	date_of_birth = models.DateField(null=True)
	nationality = models.CharField(max_length=200);					#FIXME: Esse campo deve ter valores pré definidos.

	def __unicode__(self):
		return "%s %s (%s)" % (self.name, self.lastname, self.email)

class Address(models.Model):
	zipcode = models.CharField(max_length=9);
	address1 = models.CharField(max_length=200);					# Rua
	address2 = models.CharField(max_length=200);					# Complemento
	number = models.DecimalField(max_digits=10, decimal_places=0)
	district = models.CharField(max_length=200);					# Bairro
	city = models.CharField(max_length=200);
	state = models.CharField(max_length=200);
	patient = models.OneToOneField(Patient, null=True, blank=True)

	def __unicode__(self):
		return "%s, %s (%s)" % (self.address1, self.number, self.city)

