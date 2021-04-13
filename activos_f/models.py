# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models import F
from django.db.models import Sum
from django.db.models import Avg
import datetime
from contabilidad.models import *
from almacenes.models import *
from dateutil.relativedelta import relativedelta
from decimal import Decimal

import re

def validate_file_extension(value):
	import os
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.gif','.jpeg','.jpg']
	if not ext in valid_extensions:
		raise ValidationError(u'Tipo de Archivo no Soportado!')

def validate_image(image):
	file_size = image.file.size
	limit_kb = 200
	if file_size > limit_kb*1024:
		raise ValidationError(u"El tamaño máximo permitido es de 200 KB")

class Rubro(models.Model):
	num_cuenta = models.OneToOneField('contabilidad.nivel_cinco')
	prefijo = models.CharField(
		max_length=7,
		null=False,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido'
				)
			]
		)
	nombre = models.CharField(
		max_length=40,
		null=False,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido'
				)
			]
		)
	vida_util = models.PositiveIntegerField(
		null=False,
		blank=False
		)
	coeficiente = models.DecimalField(
		default=0,
		max_digits=5,
		decimal_places=2,
		null=False,
		blank=False
		)
	actualiza = models.BooleanField(
		default=False
		)
	deprecia = models.BooleanField(
		default=False
		)

	def __unicode__(self):
		return self.nombre

	def nomb(self):
		return self.nombre

	def val_ini_excel(self, f, f1):
		res = Alta_baja_activo.objects.filter(fecha_alta__range=(f, f1), tipo_bien__rubro=self).aggregate(total=Sum('valor_inic'))
		return res['total']

	def val_inic_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.valor_inicial(fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.valor_inicial_cap(fecha_ant)
		result = res + res2
		return round(result, 2)

	def valor_actual_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.valor_actual(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.valor_actual_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def actualizacion_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.actualizacion(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.actualizacion_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def deprec_gestion_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.deprec_gestion(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.deprec_gestion_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def deprec_acum_inicial_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.deprec_acum_inicial(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.deprec_acum_inicial_cap(fecha, fecha_ant)
		result = res + res2
		return round(result, 2)

	def valor_act_deprec_acum_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.valor_act_deprec_acum(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.valor_act_deprec_acum_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def actualiz_deprec_acum_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.actualiz_deprec_acum(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.actualiz_deprec_acum_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def deprec_acum_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.deprec_acum(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.deprec_acum_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def saldo_activo_tot_excel(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self, vinculado=False, baja=False)
		for i in res1:
			res = res + i.saldo_activo(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self, fecha_cap__lte=fecha):
				res2 = res2 + j.saldo_activo_cap(fecha, fecha_ant)
		result = res + res2
		return result

class Tipo_bien(models.Model):
	rubro = models.ForeignKey(Rubro)
	codigo = models.CharField(
		default='0',
		max_length=12,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo sólo debe contener números',
				code='Numero Invalido'
				)
			]
		)
	tipo = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
				)
			]
		)
	marca = models.CharField(
		max_length=100,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
				)
			]
		)
	modelo = models.CharField(
		max_length=100,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
				)
			]
		)
	caracter = models.CharField(
		max_length=500,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
				)
			]
		)
	color = models.CharField(
		max_length=30,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
				)
			]
		)
	serie = models.CharField(
		max_length=300,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
				)
			]
		)

	def __unicode__(self):
		return self.tipo

class personal_aut_act(models.Model):
	personal = models.ForeignKey('usuarios.personal')
	alta_activo = models.ForeignKey('Alta_baja_activo')

class Ubicacion_gen(models.Model):
	ubicacion_g = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
			)
		]
	)
	def __unicode__(self):
		return self.ubicacion_g

class Alta_baja_activo(models.Model):
	personal = models.ManyToManyField('usuarios.personal', through='personal_aut_act')
	tipo_bien = models.ForeignKey(Tipo_bien)
	ubicacion = models.ForeignKey(Ubicacion_gen)
	codigo = models.CharField(
		default='0',
		max_length=20,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
				)
			]
		)
	tipo_alta = models.CharField(
		max_length=1,
		blank=False,
		null=False,
		choices=(('1','Bienes Nuevos'),('2','Bienes Usados'))
		)
	fecha_alta = models.DateField(
		null=False,
		blank=False
		)
	moneda = models.CharField(
		max_length=1,
		blank=False,
		null=False,
		choices=(('1','Bs.'),('2','$us.'))
		)
	valor_inic = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False
		)
	cantidad = models.PositiveIntegerField(
		null=False,
		)
	deprec = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False
		)
	vida_util = models.PositiveIntegerField(
		null=False,
		blank=False,
		default=0
		)
	vida_util_rest = models.PositiveIntegerField(
		null=False,
		blank=False,
		default=0
		)
	estado_bien = models.CharField(
		max_length=1,
		blank=False,
		null=False,
		choices=(('N','Nuevo'),('B','Bueno'),('R','Regular'),('M','Malo'),('O','Obsoleto y/o Pésimo'))
		)
	descripcion = models.CharField(
		max_length=70,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener letras y números',
				code='Numero Invalido'
				)
			]
		)
	img_activo = models.ImageField(
		upload_to='activos_fijos/', 
		validators=[validate_file_extension, validate_image],
		null=True,
		blank=True
	)
	vinculado = models.BooleanField(
		default=False
		)
	fecha_baja = models.DateField(
		blank=True,
		null=True
		)
	razon_baja = models.CharField(
		max_length=2,
		blank=True,
		choices=(('1','Enajenación'),('2','Hurto, robo o pérdida fortuita'),('3','Mermas'),('4','Vencimiento, descomposiciones, alteraciones y deterioros'),('5','Inutilización u obsolencia'),('6','Reconstrucción de edificaciones, desmantelamiento total o parcial'),('7','Reacondicionamiento o transformación física'),('8','Siniestros'),('9','Error de transcripción'),('10','Otros'))
		)
	baja = models.BooleanField(
		default=False
		)
	estado = models.BooleanField(
		default=False
		)

	def __unicode__(self):
		return "Activo: " + unicode(self.tipo_bien) + " Ubicación: " + unicode(self.ubicacion) + " Fecha_alta: " + str(self.fecha_alta) + " Valor inicial: " + str(self.valor_inic)

	def cap(self, fecha):
		return self.capitalizacion_set.filter(alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha)

	def val_ini(self, f, f1):
		res = Alta_baja_activo.objects.filter(fecha_alta__range=(f, f1), tipo_bien__rubro=self.tipo_bien.rubro).aggregate(total=Sum('valor_inic'))
		return res['total']

	def cant_material(self):
		return Capitalizacion.objects.filter(alta_activo=self.id).count()

	def fecha_alt(self):
		return self.fecha_alta.strftime("%d/%m/%y")

	def fecha_baj(self):
		return self.fecha_baja.strftime("%d/%m/%y")

	def factor(self, fecha, fecha_ant):
		f = self.fecha_alta
		meses = abs((fecha.year - f.year) * 12 + fecha.month - f.month)
		if (f > fecha_ant) & (f < fecha):
			ufv_prim = Cotizacion.objects.get(fecha=f).ufv
		else:
			ufv_prim = Cotizacion.objects.get(fecha=fecha_ant).ufv
		if meses >= self.vida_util_rest:
			f1 = f + relativedelta(months=self.vida_util_rest)
			ufv_ult = Cotizacion.objects.get(fecha=f1).ufv
		else:
			ufv_ult = Cotizacion.objects.get(fecha=fecha).ufv

		
		aux = ufv_ult/ufv_prim
		res = round(aux, 7)	
		return res

	def valor_inicial(self, fecha_ant):
		f =  self.fecha_alta
		if self.fecha_alta <= fecha_ant:
			ufv_p = Cotizacion.objects.get(fecha=f).ufv
			ufv_u = Cotizacion.objects.get(fecha=fecha_ant).ufv
			aux = ufv_u/ufv_p
			aux1 = round(aux, 7)
			aux2 = self.valor_inic * aux
		else:
			aux2 = self.valor_inic
		res = aux2
		return float(res)

	def valor_inicial_r(self, fecha_ant):
		f =  self.fecha_alta
		if self.fecha_alta <= fecha_ant:
			ufv_p = Cotizacion.objects.get(fecha=f).ufv
			ufv_u = Cotizacion.objects.get(fecha=fecha_ant).ufv
			aux = ufv_u/ufv_p
			aux1 = round(aux, 7)
			aux2 = self.valor_inic * aux
		else:
			aux2 = self.valor_inic
		res = round(aux2, 2)
		return float(res)

	def valor_actual(self, fecha, fecha_ant):
		res = self.factor(fecha, fecha_ant) * self.valor_inicial(fecha_ant)
		return round(res, 2)

	def actualizacion(self, fecha, fecha_ant):
		res = self.valor_actual(fecha, fecha_ant) - self.valor_inicial(fecha_ant)
		return round(res, 2)

	def depreciacion(self):
		res = self.tipo_bien.rubro.coeficiente/100
		return round(float(res), 2)

	def deprec_gestion(self, fecha, fecha_ant):
		f = self.fecha_alta
		try:
			aux = 1/self.cant_material()
		except Exception as e:
			aux = 1
		cant = round(aux, 2)
		meses = abs((fecha.year - f.year) * 12 + fecha.month - f.month)
		if meses >= self.vida_util_rest:
			f1 = f + relativedelta(months=self.vida_util_rest)
			meses_res = abs((f1.year - fecha_ant.year) * 12 + f1.month - fecha_ant.month)
			res = (self.valor_actual(fecha, fecha_ant) * self.depreciacion() / 12 * (meses_res+1)) - cant
		elif f > fecha_ant:
			meses1 = abs((fecha.year - f.year) * 12 + fecha.month - f.month)
			res = self.valor_actual(fecha, fecha_ant) * self.depreciacion() / 12 * (meses1+1)
		else:
			res = self.valor_actual(fecha, fecha_ant) * self.depreciacion()
		return round(res, 2)

	def deprec_acum_inicial(self, fecha, fecha_ant):
		f =  self.fecha_alta
		if self.deprec == 0:
			if f > fecha_ant:
				res = 0
			else:
				try:
					aux = 1/self.cant_material()
				except Exception as e:
					aux = 1
				cant = round(aux, 2)
				meses = abs((fecha_ant.year - f.year) * 12 + fecha_ant.month - f.month)
				if meses >= self.vida_util_rest:
					f1 = f + relativedelta(months=self.vida_util_rest)
					meses_res = abs((f1.year - f.year) * 12 + f1.month - f.month)
					res = (self.valor_actual(fecha, fecha_ant) * self.depreciacion() / 12 * (meses_res+1)) - cant
				elif f < fecha_ant:
					meses1 = abs((fecha_ant.year - f.year) * 12 + fecha_ant.month - f.month)
					res = self.valor_actual(fecha_ant, fecha) * self.depreciacion() / 12 * (meses1+1)
				else:
					res = self.valor_actual(fecha_ant, fecha) * self.depreciacion()
		else:
			res = self.deprec
		return float(res)

	def deprec_acum_inicial_r(self, fecha, fecha_ant):
		f =  self.fecha_alta
		if self.deprec == 0:
			if f > fecha_ant:
				res = 0
			else:
				try:
					aux = 1/self.cant_material()
				except Exception as e:
					aux = 1
				cant = round(aux, 2)
				meses = abs((fecha_ant.year - f.year) * 12 + fecha_ant.month - f.month)
				if meses >= self.vida_util_rest:
					f1 = f + relativedelta(months=self.vida_util_rest)
					meses_res = abs((f1.year - f.year) * 12 + f1.month - f.month)
					res = (self.valor_actual(fecha, fecha_ant) * self.depreciacion() / 12 * (meses_res+1)) - cant
				elif f < fecha_ant:
					meses1 = abs((fecha_ant.year - f.year) * 12 + fecha_ant.month - f.month)
					res = self.valor_actual(fecha_ant, fecha) * self.depreciacion() / 12 * (meses1+1)
				else:
					res = self.valor_actual(fecha_ant, fecha) * self.depreciacion()
		else:
			res = self.deprec
		return round(res, 2)

	def valor_act_deprec_acum(self, fecha, fecha_ant):
		res = self.deprec_acum_inicial(fecha, fecha_ant) * self.factor(fecha, fecha_ant)
		
		return round(res, 2)

	def actualiz_deprec_acum(self, fecha, fecha_ant):
		res = self.valor_act_deprec_acum(fecha, fecha_ant) - self.deprec_acum_inicial(fecha, fecha_ant)
		return round(res, 2)

	def deprec_acum(self, fecha, fecha_ant):
		res = self.valor_act_deprec_acum(fecha, fecha_ant) + self.deprec_gestion(fecha, fecha_ant)
		return round(res, 2)

	def saldo_activo(self, fecha, fecha_ant):
		res = self.valor_actual(fecha, fecha_ant) - self.deprec_acum(fecha, fecha_ant)
		return round(res, 2)

	def val_inic_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.valor_inicial(fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.valor_inicial_cap(fecha_ant)
		result = res + res2
		return round(result, 2)

	def valor_actual_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.valor_actual(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.valor_actual_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def actualizacion_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.actualizacion(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.actualizacion_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def deprec_gestion_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.deprec_gestion(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.deprec_gestion_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def deprec_acum_inicial_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.deprec_acum_inicial(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.deprec_acum_inicial_cap(fecha, fecha_ant)
		result = res + res2
		return round(result, 2)

	def valor_act_deprec_acum_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.valor_act_deprec_acum(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.valor_act_deprec_acum_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def actualiz_deprec_acum_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.actualiz_deprec_acum(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.actualiz_deprec_acum_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def deprec_acum_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.deprec_acum(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.deprec_acum_cap(fecha, fecha_ant)
		result = res + res2
		return result

	def saldo_activo_tot(self, fecha, fecha_ant, vinc):
		res = 0
		res2 = 0
		if vinc == '1':
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=True, baja=False)
		else:
			res1 = Alta_baja_activo.objects.filter(fecha_alta__lte=fecha, tipo_bien__rubro=self.tipo_bien.rubro, vinculado=False, baja=False)
		for i in res1:
			res = res + i.saldo_activo(fecha, fecha_ant)
			for j in i.capitalizacion_set.filter(alta_activo__fecha_alta__lte=fecha, alta_activo__tipo_bien__rubro=self.tipo_bien.rubro, fecha_cap__lte=fecha):
				res2 = res2 + j.saldo_activo_cap(fecha, fecha_ant)
		result = res + res2
		return result

class Capitalizacion(models.Model):
	alta_activo = models.ForeignKey('Alta_baja_activo')
	item = models.ForeignKey('almacenes.item')
	valor_inic = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False
		)
	fecha_cap = models.DateField(
		null=False,
		blank=False
		)
	estado = models.BooleanField(
		default=False
		)

	def fecha_f(self):
		return self.fecha_cap.strftime("%d/%m/%y")

	def factor_cap(self, fecha, fecha_ant):
		f = self.fecha_cap
		meses = abs((fecha.year - f.year) * 12 + fecha.month - f.month)
		if meses >= self.alta_activo.vida_util_rest:
			res = self.alta_activo.factor(fecha, fecha_ant)
		else:
			if (f > fecha_ant) & (f < fecha):
				ufv_prim = Cotizacion.objects.get(fecha=f).ufv
			else:
				ufv_prim = Cotizacion.objects.get(fecha=fecha_ant).ufv
			ufv_ult = Cotizacion.objects.get(fecha=fecha).ufv
			aux = ufv_ult/ufv_prim
			res = round(aux, 7)
		return res

	def valor_inicial_cap(self, fecha_ant):
		f = self.fecha_cap
		if self.fecha_cap <= fecha_ant:
			ufv_p = Cotizacion.objects.get(fecha=f).ufv
			ufv_u = Cotizacion.objects.get(fecha=fecha_ant).ufv
			aux = ufv_u/ufv_p
			aux1 = round(aux, 7)
			res = self.valor_inic * aux
		else:
			res = self.valor_inic
		return float(res)

	def valor_inicial_cap_r(self, fecha_ant):
		f = self.fecha_cap
		if self.fecha_cap <= fecha_ant:
			ufv_p = Cotizacion.objects.get(fecha=f).ufv
			ufv_u = Cotizacion.objects.get(fecha=fecha_ant).ufv
			aux = ufv_u/ufv_p
			aux1 = round(aux, 7)
			res = self.valor_inic * aux
		else:
			res = self.valor_inic
		return round(float(res), 2)

	def valor_actual_cap(self, fecha, fecha_ant):
		res = self.factor_cap(fecha, fecha_ant) * self.valor_inicial_cap(fecha_ant)
		return round(res, 2)

	def actualizacion_cap(self, fecha, fecha_ant):
		res = self.valor_actual_cap(fecha, fecha_ant) - self.valor_inicial_cap(fecha_ant)
		return res

	def depreciacion_cap(self):
		f = self.fecha_cap
		f1 = self.alta_activo.fecha_alta
		meses = abs((f.year - f1.year) * 12 + f.month - f1.month)
		res = 12.0/(self.alta_activo.vida_util_rest - (meses - 1))
		return res

	def depreciacion_cap_r(self):
		f = self.fecha_cap
		f1 = self.alta_activo.fecha_alta
		meses = abs((f.year - f1.year) * 12 + f.month - f1.month)
		res = 12.0/(self.alta_activo.vida_util_rest - (meses - 1))
		return round(res, 2)

	def deprec_gestion_cap(self, fecha, fecha_ant):
		f = self.alta_activo.fecha_alta
		f1 = self.fecha_cap
		try:
			aux = 1/self.alta_activo.cant_material()
		except Exception as e:
			aux = 1
		cant = round(aux, 2)
		meses = abs((fecha.year - f.year) * 12 + fecha.month - f.month)
		f2 = f + relativedelta(months=self.alta_activo.vida_util_rest)
		meses_res = abs((f2.year - fecha_ant.year) * 12 + f2.month - fecha_ant.month)
		if meses >= self.alta_activo.vida_util_rest:
			res = (self.valor_actual_cap(fecha, fecha_ant) * self.depreciacion_cap() / 12 * (meses_res+1)) - cant
		elif f1 > fecha_ant:
			meses1 = abs((fecha.year - f1.year) * 12 + fecha.month - f1.month)
			res = self.valor_actual_cap(fecha, fecha_ant) * self.depreciacion_cap() / 12 * (meses1+1)
		else:
			res = self.valor_actual_cap(fecha, fecha_ant) * self.depreciacion_cap()
		return round(res, 2)

	def deprec_acum_inicial_cap(self, fecha, fecha_ant):
		f =  self.fecha_cap
		if f > fecha_ant:
			res = 0
		else:
			try:
				aux = 1/self.alta_activo.cant_material()
			except Exception as e:
				aux = 1
			cant = round(aux, 2)
			meses = abs((fecha_ant.year - f.year) * 12 + fecha_ant.month - f.month)
			if meses >= self.alta_activo.vida_util_rest:
				f1 = f + relativedelta(months=self.alta_activo.vida_util_rest)
				meses_res = abs((f1.year - f.year) * 12 + f1.month - f.month)
				res = (self.valor_actual_cap(fecha_ant, fecha) * self.depreciacion_cap() / 12 * (meses_res+1)) - cant
			elif f < fecha_ant:
				meses1 = abs((fecha_ant.year - f.year) * 12 + fecha_ant.month - f.month)
				res = self.valor_actual_cap(fecha_ant, fecha) * self.depreciacion_cap() / 12 * (meses1+1)
			else:
				res = self.valor_actual_cap(fecha_ant, fecha) * self.depreciacion_cap()
		return res

	def deprec_acum_inicial_cap_r(self, fecha, fecha_ant):
		f =  self.fecha_cap
		if f > fecha_ant:
			res = 0
		else:
			try:
				aux = 1/self.alta_activo.cant_material()
			except Exception as e:
				aux = 1
			cant = round(aux, 2)
			meses = abs((fecha_ant.year - f.year) * 12 + fecha_ant.month - f.month)
			if meses >= self.alta_activo.vida_util_rest:
				f1 = f + relativedelta(months=self.alta_activo.vida_util_rest)
				meses_res = abs((f1.year - f.year) * 12 + f1.month - f.month)
				res = (self.valor_actual_cap(fecha_ant, fecha) * self.depreciacion_cap() / 12 * (meses_res+1)) - cant
			elif f < fecha_ant:
				meses1 = abs((fecha_ant.year - f.year) * 12 + fecha_ant.month - f.month)
				res = self.valor_actual_cap(fecha_ant, fecha) * self.depreciacion_cap() / 12 * (meses1+1)
			else:
				res = self.valor_actual_cap(fecha_ant, fecha) * self.depreciacion_cap()
		return round(res, 2)

	def valor_act_deprec_acum_cap(self, fecha, fecha_ant):
		res = self.deprec_acum_inicial_cap(fecha, fecha_ant) * self.factor_cap(fecha, fecha_ant)
		return round(res, 2)

	def actualiz_deprec_acum_cap(self, fecha, fecha_ant):
		res = self.valor_act_deprec_acum_cap(fecha, fecha_ant) - self.deprec_acum_inicial_cap(fecha, fecha_ant)
		return res

	def deprec_acum_cap(self, fecha, fecha_ant):
		res = self.valor_act_deprec_acum_cap(fecha, fecha_ant) + self.deprec_gestion_cap(fecha, fecha_ant)
		return res

	def saldo_activo_cap(self, fecha, fecha_ant):
		res = self.valor_actual_cap(fecha, fecha_ant) - self.deprec_acum_cap(fecha, fecha_ant)
		return res
