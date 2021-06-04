# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.contrib.auth.models import User
from usuarios import apps

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


from django.db import models



class kardex(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	ci = models.CharField(
		max_length=9,
		null=False,
		blank=False,
		unique=True,
		help_text='El CI solo debe contener un maximo de 7 digitos y opcionalmente 2 letras mas',
		validators=[
			RegexValidator(
				regex=r'[0-9]{7}[a-zA-Z]{0,2}',
				message='El CI Tiene un máximo de 7 digitos y en algunos casos dos letras mas',
				code='Numero Invalido'
				)
			]
		)
	telefono_celular = models.PositiveIntegerField(
		null=False,
		blank=False,
		unique=True,
		help_text='El telefono celular solo debe contener un maximo de 8 digitos',
		validators=[
			RegexValidator(
				regex=r'^[0-9]{8}$',
				message='Telefono celular (Solo 8 digitos)',
				code='Numero Invalido')
			]
		)
	telefono_fijo = models.PositiveIntegerField(
		null=False,
		blank=False,
		help_text='El telefono celular solo debe contener un maximo de 7 digitos',
		validators=[
			RegexValidator(
				regex=r'^[0-9]{7}',
				message='Telefono fijo (Solo 7 digitos)',
				code='Numero Invalido'
				)
			]
		)
	direccion = models.CharField(
		max_length=50,
		null=False,
		blank=False
		)
	profesion = models.CharField(
		max_length=45,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]{3,}$',
				message='El campo profesion debe contener solo letras',
				code='Numero Invalido'
				)
			]
		)

		#def __str__(self):
		#return '{}{}'.format(self.ci);
			#return (self.ci)
class cargo(models.Model):
	nombre_cargo = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			# validadores de filas
			RegexValidator(
				regex=r'^(([a-zA-ZñÑáéíóúÁÉÍÓÚ]{2,} )||([a-zA-ZñÑáéíóúÁÉÍÓÚ]{2,}))+$',
				message='El cargo deve contener solo letras y un minimo de dos caracteres',
				code='Numero Invalido'
			)
		]
	)
	def __str__(self):
		#return '{}{}'.format(self.nombre_cargo)
		return (self.nombre_cargo)

class personal(models.Model):
	nombre = models.CharField(
		max_length=60,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido'
				)
			]
		)
	ap_paterno = models.CharField(
		max_length=60,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido'
				)
			]
		)
	ap_materno = models.CharField(
		max_length=60,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido'
				)
			]
		)
	ci = models.CharField(
		max_length=9,
		null=False,
		blank=False,
		help_text='El CI solo debe contener un maximo de 7 digitos y opcionalmente 2 letras mas',
		validators=[
			RegexValidator(
				regex=r'^[0-9]{6,8}$',
				message='El campo sólo debe contener números y un máximo de 8 dígitos',
				code='Numero Invalido'
				)
			]
		)
	cargo = models.CharField(
		max_length=30,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido'
				)
			]
		)
	telefono = models.CharField(
		max_length=10,
		null=False, 
		blank=False,
		help_text='El teléfono solo debe contener un maximo de 8 digitos', 
		validators=[
			RegexValidator(
				regex=r'^[0-9]{7,8}$', 
				message='El teléfono tiene un máximo de 8 dígitos', 
				code='Numero Invalido'
			)
		]
	)
	email = models.EmailField(
		blank=True,
		help_text='Por ej. mindes@gmail.com'
	)
	direccion = models.CharField(
		max_length=50,
		null=False,
		blank=False
	)
	fecha_ingreso = models.DateField(
		null=False,
		blank=False
		)
	def fecha_f(self):
		return self.fecha_ingreso.strftime("%d/%m/%y")

	def __unicode__(self):
		return self.nombre + " " + self.ap_paterno + " " + self.ap_materno