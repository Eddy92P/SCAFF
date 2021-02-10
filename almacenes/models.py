# -*- coding: utf-8 -*-
from django.db import models
from django.apps import apps
from django.utils.translation import ugettext_lazy as _
#from apps.seguimiento.models import item

from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models import F
from django.db.models import Sum
from django.db.models import Avg

import re

# Create your models here.
class proveedor(models.Model):
	nombre = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido'
			)
		]
	)
	ciudad = models.CharField(
		max_length=30,
		blank=False,
		null=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido'
				)
			]
	)
	nit = models.CharField(
		default='0',
		max_length=50,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{9,12}$', 
				message='El NIT tiene un maximo de 12 dígitos, además de contener sólo números', 
				code='Numero Invalido'
			)
		]
	)
	telefono = models.CharField(
		max_length=10,
		null=False, 
		blank=False, 
		validators=[
			RegexValidator(
				regex=r'^[0-9]{7,8}$', 
				message='El teléfono tiene un máximo de 8 dígitos, además de contener sólo números', 
				code='Numero Invalido'
			)
		]
	)
	email = models.EmailField(
		blank=True
	)
	direccion = models.CharField(
		max_length=50,
		null=False,
		blank=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = _('proveedores')

class cliente(models.Model):
	ubicacion_gen = models.ForeignKey('activos_f.Ubicacion_gen')
	num_cuenta = models.ForeignKey('contabilidad.nivel_cinco')
	nombre = models.CharField(
		max_length=80,
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
	referencia = models.CharField(
		max_length=500,
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
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = _('clientes')

class tipo_entrada(models.Model):
	nombre = models.CharField(
		max_length=50,
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
	def __unicode__(self):
		return self.nombre

class tipo_salida(models.Model):
	nombre = models.CharField(
		max_length=50,
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
	def __unicode__(self):
		return self.nombre

class unidad(models.Model):
	simbolo = models.CharField(
		max_length=5,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)
	descripcion = models.CharField(
		max_length=50,
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

	def __unicode__(self):
		return self.simbolo

"""class almacen(models.Model):
	nombre = models.CharField(
		max_length=80,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)"""

"""def items(self):
		item = apps.get_model('seguimiento', 'item')
		return item.objects.filter(proyecto__ubicacion_proyecto=str(self.ciudad))"""
"""def __unicode__(self):
		return self.nombre

	def total_cant_e(self, f1, f2):
		res = item.objects.filter(almacen=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_cant_s(self, f1, f2):
		res = item.objects.filter(almacen=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def almacen_a_ent(self, f1):
		res = item.objects.filter(almacen=self, ingresoitem__encingresoitem__fecha__lt=f1).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def almcen_a_sal(self, f1):
		res = item.objects.filter(almacen=self, salidaitem__encsalidaitem__fecha__lt=f1).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def almacen_a_t(self, f1):
		res = self.almacen_a_ent(f1) - self.almcen_a_sal(f1)
		return res

	def total_alm_e(self, f1, f2):
		res = item.objects.filter(almacen=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_alm_s(self, f1, f2):
		res = item.objects.filter(almacen=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def almacen_t(self, f1, f2):
		res = self.almacen_a_t(f1) + self.total_alm_e(f1, f2) - self.total_alm_s(f1, f2)
		return res

	#Reporte detalle de entradas
	def importe_total_s(self, f1, f2):
		res = item.objects.filter(almacen=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_total(self, f1, f2):
		res = item.objects.filter(almacen=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__costo_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_total_iva(self, f1, f2):
		res = item.objects.filter(almacen=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total'] 

	def importe_iva(self, f1, f2):
		res = self.importe_total(f1, f2) - self.importe_total_iva(f1, f2)
		return res"""

class categoria(models.Model):
	num_cuenta = models.OneToOneField('contabilidad.nivel_cinco')
	nombre = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)

	def total_cant_e(self, f1, f2):
		res = item.objects.filter(categoria=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_cant_s(self, f1, f2):
		res = item.objects.filter(categoria=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def categoria_a_ent(self, f1):
		res = item.objects.filter(categoria=self, ingresoitem__encingresoitem__fecha__lt=f1).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def categoria_a_sal(self, f1):
		res = item.objects.filter(categoria=self, salidaitem__encsalidaitem__fecha__lt=f1).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def categoria_a_t(self, f1):
		res = self.categoria_a_ent(f1) - self.categoria_a_sal(f1)
		return res

	def total_categ_e(self, f1, f2):
		res = item.objects.filter(categoria=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_categ_s(self, f1, f2):
		res = item.objects.filter(categoria=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def categoria_t(self, f1, f2):
		res = self.categoria_a_t(f1) + self.total_categ_e(f1, f2) - self.total_categ_s(f1, f2)
		return res

	#Reporte detalle de entradas
	def importe_total_s(self, f1, f2):
		res = item.objects.filter(categoria=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_total(self, f1, f2):
		res = item.objects.filter(categoria=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__costo_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_total_iva(self, f1, f2):
		res = item.objects.filter(categoria=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total'] 

	def importe_iva(self, f1, f2):
		res = self.importe_total(f1, f2) - self.importe_total_iva(f1, f2)
		return res

	def __unicode__(self):
		return self.nombre

class subcategoria(models.Model):
	categoria = models.ForeignKey(categoria)
	nombre = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)
	codigo = models.CharField(
		max_length=4,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo sólo debe contener números',
				code='Numero Invalido'
				)
			]
		)


	def total_cant_e(self, f1, f2):
		res = item.objects.filter(subcategoria=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_cant_s(self, f1, f2):
		res = item.objects.filter(subcategoria=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subcategoria_a_ent(self, f1):
		res = item.objects.filter(subcategoria=self, ingresoitem__encingresoitem__fecha__lt=f1).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subcategoria_a_sal(self, f1):
		res = item.objects.filter(subcategoria=self, salidaitem__encsalidaitem__fecha__lt=f1).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subcategoria_a_t(self, f1):
		res = self.subcategoria_a_ent(f1) - self.subcategoria_a_sal(f1)
		return res

	def total_sub_e(self, f1, f2):
		res = item.objects.filter(subcategoria=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_sub_s(self, f1, f2):
		res = item.objects.filter(subcategoria=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subcategoria_t(self, f1, f2):
		res = self.subcategoria_a_t(f1) + self.total_sub_e(f1, f2) - self.total_sub_s(f1, f2)
		return res

	#Reporte detalle de entradas
	def importe_total_s(self, f1, f2):
		res = item.objects.filter(subcategoria=self, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_total(self, f1, f2):
		res = item.objects.filter(subcategoria=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__costo_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_total_iva(self, f1, f2):
		res = item.objects.filter(subcategoria=self, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total'] 

	def importe_iva(self, f1, f2):
		res = self.importe_total(f1, f2) - self.importe_total_iva(f1, f2)
		return res

	def __unicode__(self):
		return self.nombre

class item(models.Model):
	categoria = models.ForeignKey(categoria)
	subcategoria = models.ForeignKey(subcategoria)
	unidad = models.ForeignKey(unidad)
	codigo = models.CharField(
		max_length=15,
		unique=False,
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
	nombre = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)
	activo_f = models.BooleanField(
		default=False
		)
	minimo = models.FloatField(
		null=False
		)
	maximo = models.FloatField(
		null = False)

	#def cod_item(self):
		#res = str(self.subcategoria.categoria.almacen.id) + '-' + str(self.subcategoria.categoria.id) + '-' + str(self.subcategoria.id) + '-' + self.codigo.zfill(4)
		#return res

	#Cálculo de saldos anteriores
	def cant_ea(self, f1):
		res = item.objects.filter(id=self.id, ingresoitem__encingresoitem__fecha__lt=f1).aggregate(total=Sum('ingresoitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def cant_sa(self, f1):
		res = item.objects.filter(id=self.id, salidaitem__encsalidaitem__fecha__lt=f1).aggregate(total=Sum('salidaitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subt_ea(self, f1):
		res = item.objects.filter(id=self.id, ingresoitem__encingresoitem__fecha__lt=f1).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subt_sa(self, f1):
		res = item.objects.filter(id=self.id, salidaitem__encsalidaitem__fecha__lt=f1).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_cant_a(self, f1):
		res = self.cant_ea(f1) - self.cant_sa(f1)
		return res

	def total_subt_a(self, f1):
		res = self.subt_ea(f1) - self.subt_sa(f1)
		return res

	#Saldos anteriores de almacenes, categorias, sub_categorias
	
	def categoria_a_ent(self, f1):
		res = item.objects.filter(categoria=self.categoria, ingresoitem__encingresoitem__fecha__lt=f1).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def categoria_a_sal(self, f1):
		res = item.objects.filter(categoria=self.categoria, salidaitem__encsalidaitem__fecha__lt=f1).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def categoria_a_t(self, f1):
		res = self.categoria_a_ent(f1) - self.categoria_a_sal(f1)
		return res

	def subcategoria_a_ent(self, f1):
		res = item.objects.filter(subcategoria=self.subcategoria, ingresoitem__encingresoitem__fecha__lt=f1).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subcategoria_a_sal(self, f1):
		res = item.objects.filter(subcategoria=self.subcategoria, salidaitem__encsalidaitem__fecha__lt=f1).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subcategoria_a_t(self, f1):
		res = self.subcategoria_a_ent(f1) - self.subcategoria_a_sal(f1)
		return res 

	#Cálculo de cantidades, sub_totales y saldos actuales
	def total_costo_u_s(self, f1, f2):
		res = item.objects.filter(id=self.id, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__costo_unit'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_cant_e(self, f1, f2):
		res = item.objects.filter(id=self.id, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_cant_s(self, f1, f2):
		res = item.objects.filter(id=self.id, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_subt_e(self, f1, f2):
		res = item.objects.filter(id=self.id, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_subt_s(self, f1, f2):
		res = item.objects.filter(id=self.id, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def total_cant(self, f1, f2):
		res = self.total_cant_a(f1) + self.total_cant_e(f1, f2) - self.total_cant_s(f1, f2)
		return res

	def total_subt(self, f1, f2):
		res = self.total_subt_a(f1) + self.total_subt_e(f1, f2) - self.total_subt_s(f1, f2)
		return res

	def total_sub_e(self, f1, f2):
		res = item.objects.filter(subcategoria=self.subcategoria, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']
	
	def total_categ_e(self, f1, f2):
		res = item.objects.filter(categoria=self.categoria, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']
	


	def total_sub_s(self, f1, f2):
		res = item.objects.filter(subcategoria=self.subcategoria, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']
	
	def total_categ_s(self, f1, f2):
		res = item.objects.filter(categoria=self.categoria, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def categoria_t(self, f1, f2):
		res = self.categoria_a_t(f1) + self.total_categ_e(f1, f2) - self.total_categ_s(f1, f2)
		return res

	def subcategoria_t(self, f1, f2):
		res = self.subcategoria_a_t(f1) + self.total_sub_e(f1, f2) - self.total_sub_s(f1, f2)
		return res

	def importe_total_s(self, f1, f2):
		res = item.objects.filter(id=self.id, salidaitem__encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_total_e(self, f1, f2):
		res = item.objects.filter(id=self.id, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__costo_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_total_iva(self, f1, f2):
		res = item.objects.filter(id=self.id, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total'] 

	def importe_iva(self, f1, f2):
		res = self.importe_total_e(f1, f2) - self.importe_total_iva(f1, f2)
		return res

	#Totales
	def ingreso_t_a(self, f1):
		res = ingresoitem.objects.filter(encingresoitem__fecha__lt=f1).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def salida_t_a(self, f1):
		res = salidaitem.objects.filter(encsalidaitem__fecha__lt=f1).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subtotal_t_a(self, f1):
		res = self.ingreso_t_a(f1) - self.salida_t_a(f1)
		return res

	def ingreso_t(self, f1, f2):
		res = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def salida_t(self, f1, f2):
		res = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def saldo_t(self, f1, f2):
		res = self.subtotal_t_a(f1) + self.ingreso_t(f1, f2) - self.salida_t(f1, f2)
		return res

	#Totales solo una categoría
	def ingresocat_t_a(self, f1, c):
		res = ingresoitem.objects.filter(encingresoitem__fecha__lt=f1, item__subcategoria=c).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def salidacat_t_a(self, f1, c):
		res = salidaitem.objects.filter(encsalidaitem__fecha__lt=f1, item__categoria=c).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def subtotalcat_t_a(self, f1, c):
		res = self.ingresocat_t_a(f1, c) - self.salidacat_t_a(f1, c)
		return res

	def ingresocat_t(self, f1, f2, c):
		res = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2), item__categoria=c).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def salidacat_t(self, f1, f2, c):
		res = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2), item__categoria=c).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def saldocat_t(self, f1, f2, c):
		res = self.subtotalcat_t_a(f1, c) + self.ingresocat_t(f1, f2, c) - self.salidacat_t(f1, f2, c)
		return res

	def __unicode__(self):
		try:
		 	return str(self.codigo) + " " + self.nombre + " " + "(" +self.unidad.simbolo + ")" + " " + "-" + " cant. almacen " + str(self.itemalmacen_set.all().get().cantidad) + "(" + self.unidad.simbolo + ")"
		except Exception as e:
			return str(self.codigo) + " " + self.nombre + " " + "(" +self.unidad.simbolo + ")" + " " + "-" + " cant. almacen " + '0' + "(" + self.unidad.simbolo + ")"

class item_act(models.Model):
	item = models.OneToOneField(item)
	tipo_bien = models.ForeignKey('activos_f.Tipo_bien')

class itemalmacen(models.Model):
	item = models.ForeignKey(item)
	cantidad = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	precio = models.DecimalField(
		default=0,
		max_digits=10,
		decimal_places=2,
		null=False,
		blank=False
		)

class personal_aut(models.Model):
	personal = models.ForeignKey('usuarios.personal')
	encingresoitem = models.ForeignKey('encingresoitem')

class encingresoitem(models.Model):
	tipo_entrada = models.ForeignKey(tipo_entrada)
	proveedor = models.ForeignKey(proveedor)
	personal = models.ManyToManyField('usuarios.personal', through='personal_aut')
	fecha = models.DateField(
		null=False,
		blank=False
		)
	factura = models.CharField(
		max_length=50,
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
	
	iva = models.BooleanField(
		default = False
		)
	total = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False,
		validators=[MinValueValidator(1, "El valor no puede ser cero")]
		)
	total_iva = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False,
		)
	importe_iva = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False,
		)
	concepto = models.CharField(
		max_length=200,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)
	estado = models.BooleanField(
		default=False
		)
	cerrado = models.BooleanField(default=False)

	def tipo(self):
		return "E"

	def fecha_f(self):
		return self.fecha.strftime("%d/%m/%y")

class ingresoitem(models.Model):
	encingresoitem = models.ForeignKey(encingresoitem)
	item = models.ForeignKey(item)
	cantidad = models.FloatField(
		default=0,
		null=False,
		blank=False,
		validators=[MinValueValidator(1, "El valor no puede ser cero")]
		)
	costo_total = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False,
		validators=[MinValueValidator(1, "El valor no puede ser cero")]
		)
	precio_unit = models.DecimalField(
		default=0,
		max_digits=10,
		decimal_places=2,
		null=False,
		blank=False
		)
	costo_unit = models.DecimalField(
		default=0,
		max_digits=10,
		decimal_places=2,
		null=False,
		blank=False
		)
	sub_total = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False
		)
	costo_unit_actualizado = models.DecimalField(
		default=0,
		max_digits=10,
		decimal_places=2,
		null=False,
		blank=False
		)
	sub_total_actualizado = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=False,
		blank=False
		)

	def iva(self):
		res = self.costo_total - self.sub_total
		return res

	def encabezado_f(self):
		return self.encingresoitem.fecha

	def encabezado(self):
		return self.encingresoitem

	def total(self):
		res = ingresoitem.objects.filter(item__subcategoria=self.item.subcategoria, encingresoitem__fecha=self.encingresoitem.fecha).aggregate(total=Sum('sub_total'))
		return res['total']
	
	def total1(self):
		res = ingresoitem.objects.filter(item__categoria=self.item.categoria, encingresoitem__fecha=self.encingresoitem.fecha).aggregate(total=Sum('sub_total'))
		return res['total']
	
	def total2(self):
		res = ingresoitem.objects.filter(item__almacen=self.item.almacen, encingresoitem__fecha=self.encingresoitem.fecha).aggregate(total=Sum('sub_total'))
		return res['total']

	def tipo_ent_importe(self, f1, f2):
		res = ingresoitem.objects.filter(encingresoitem__tipo_entrada=self.encingresoitem.tipo_entrada, encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('costo_total'))
		return res['total']

	def tipo_ent_costo(self, f1, f2):
		res = ingresoitem.objects.filter(encingresoitem__tipo_entrada=self.encingresoitem.tipo_entrada, encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('sub_total'))
		return res['total']

	def tipo_ent_iva(self, f1, f2):
		res = self.tipo_ent_importe(f1, f2) - self.tipo_ent_costo(f1, f2)
		return res

	#Reporte resumen entradas por Proveedor
	def cantidad_proveedor_e(self, f1, f2):
		res = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2), encingresoitem__proveedor=self.encingresoitem.proveedor).aggregate(total=Sum('cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def costo_unit_proveedor_e(self, f1, f2):
		res = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2), encingresoitem__proveedor=self.encingresoitem.proveedor).aggregate(total=Sum('costo_unit'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_proveedor_e(self, f1, f2):
		res = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2), encingresoitem__proveedor=self.encingresoitem.proveedor).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

class personal_aut_s(models.Model):
	personal = models.ForeignKey('usuarios.personal')
	encsalidaitem = models.ForeignKey('encsalidaitem')

class encsalidaitem(models.Model):
	tipo_salida = models.ForeignKey(tipo_salida)
	personal = models.ManyToManyField('usuarios.personal', through='personal_aut_s')
	cliente = models.ForeignKey(cliente)
	fecha = models.DateField(
		null=False,
		blank=False
		)
	nro_comp = models.CharField(
		max_length=50,
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
	seccion = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)
	concepto = models.CharField(
		max_length=200,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)
	estado = models.BooleanField(
		default=False
		)
	estado_act = models.BooleanField(
		default=False
		)
	cerrado = models.BooleanField(default=False)

	def tipo(self):
		return "S"

	def num_comp(self):
		res = str(self.id).zfill(10)
		return res

	def fecha_f(self):
		return self.fecha.strftime("%d/%m/%y")

	def importe(self, f1, f2):
		res = salidaitem.objects.filter(encsalidaitem=self, encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('sub_total'))
		return res['total']

	def cantidad_t(self, f1, f2):
		res = salidaitem.objects.filter(encsalidaitem=self, encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('cantidad'))
		return res['total']

class salidaitem(models.Model):
	encsalidaitem = models.ForeignKey(encsalidaitem)
	item = models.ForeignKey(item)
	cantidad = models.FloatField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1, "El valor no puede ser cero")]
		)
	costo_unit = models.DecimalField(
		default=0,
		max_digits=10,
		decimal_places=2,
		null=True,
		blank=True
		)
	sub_total = models.DecimalField(
		default=0,
		max_digits=12,
		decimal_places=2,
		null=True,
		blank=True
		)
	observaciones = models.CharField(
		max_length=200,
		blank=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo sólo debe contener números y letras',
				code='Numero Invalido'
				)
			]
		)
	estado_cap = models.BooleanField(
		default=False
		)

	def encabezado_f(self):
		return self.encsalidaitem.fecha

	def encabezado(self):
		return self.encsalidaitem

	def total(self):
		res = salidaitem.objects.filter(item__subcategoria=self.item.subcategoria, encsalidaitem__fecha=self.encsalidaitem.fecha).aggregate(total=Sum('sub_total'))
		return res['total']
	
	def total1(self):
		res = salidaitem.objects.filter(item__categoria=self.item.categoria, encsalidaitem__fecha=self.encsalidaitem.fecha).aggregate(total=Sum('sub_total'))
		return res['total']
	
	def total2(self):
		res = salidaitem.objects.filter(item__almacen=self.item.almacen, encsalidaitem__fecha=self.encsalidaitem.fecha).aggregate(total=Sum('sub_total'))
		return res['total']

	def tipo_sal_importe(self, f1, f2):
		res = salidaitem.objects.filter(encsalidaitem__tipo_salida=self.encsalidaitem.tipo_salida, encsalidaitem__fecha__range=(f1, f2)).aggregate(total=Sum('sub_total'))
		return res['total']

	#Reporte resumen salidas por Cliente
	def cantidad_cliente_s(self, f1, f2):
		res = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2), encsalidaitem__cliente=self.encsalidaitem.cliente).aggregate(total=Sum('cantidad'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def costo_unit_cliente_s(self, f1, f2):
		res = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2), encsalidaitem__cliente=self.encsalidaitem.cliente).aggregate(total=Sum('costo_unit'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def importe_cliente_s(self, f1, f2):
		res = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2), encsalidaitem__cliente=self.encsalidaitem.cliente).aggregate(total=Sum('sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']





































































































































































"""def total_alm_e(self, f1, f2):
	res = item.objects.filter(almacen=self.almacen, ingresoitem__encingresoitem__fecha__range=(f1, f2)).aggregate(total=Sum('ingresoitem__sub_total'))
	if res['total'] == None:
		return 0
	else:
		return res['total']"""
"""def almacen_a_ent(self, f1):
		res = item.objects.filter(almacen=self.almacen, ingresoitem__encingresoitem__fecha__lt=f1).aggregate(total=Sum('ingresoitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def almcen_a_sal(self, f1):
		res = item.objects.filter(almacen=self.almacen, salidaitem__encsalidaitem__fecha__lt=f1).aggregate(total=Sum('salidaitem__sub_total'))
		if res['total'] == None:
			return 0
		else:
			return res['total']

	def almacen_a_t(self, f1):
		res = self.almacen_a_ent(f1) - self.almcen_a_sal(f1)
		return res"""


"""
		
class material(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	unidad = models.CharField(
		max_length=10,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def clean(self):
		aux = re.sub(' +',' ',self.decripcion)
		self.decripcion = aux.capitalize()
	def __str__(self):
		return self.decripcion

class materialAlmacen(models.Model):
	almacen = models.ForeignKey(almacen)
	material = models.ForeignKey(material)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	def __str__(self):
		return self.material.decripcion
	class Meta:
		unique_together = (('almacen', 'material'),)

class ingresoMaterial(models.Model):
	almacen = models.ForeignKey(almacen)
	material = models.ForeignKey(material)
	proveedor = models.ForeignKey(proveedor)
	item = models.ForeignKey('seguimiento.item')
	no_factura = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{1,20}$', 
				message='El numero de factura tiene de 1 a 20 cifras', 
				code='Numero Invalido'
			)
		]
	)
	no_autorizacion = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{5,20}$', 
				message='El numero de autorizacion tiene de 5 a 20 cifras', 
				code='Numero Invalido'
			)
		]
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	def totalItem(self):
		res = ingresoMaterial.objects.filter(item=self.item).aggregate(total=Sum('costo_total'))
		return res['total']
	def total(self):
		item = apps.get_model('seguimiento', 'item')
		res = ingresoMaterial.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('costo_total'))
		return res['total']
	def unitario(self):
		return round(self.costo_total/self.cantidad,3)
		
class salidaMaterial(models.Model):
	almacen = models.ForeignKey(almacen)
	material = models.ForeignKey(material)
	confirmado = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	item = models.ForeignKey('seguimiento.item')
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)

#insumos
class insumos(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	unidad = models.CharField(
		max_length=10,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def clean(self):
		aux = re.sub(' +',' ',self.decripcion)
		self.decripcion = aux.capitalize()
	def __str__(self):
		return self.decripcion
class insumosAlmacen(models.Model):
	almacen = models.ForeignKey(almacen)
	insumos = models.ForeignKey(insumos)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	class Meta:
		unique_together = (('almacen', 'insumos'),)
class ingresoInsumos(models.Model):
	almacen = models.ForeignKey(almacen)
	insumos = models.ForeignKey(insumos)
	proveedor = models.ForeignKey(proveedor)
	item = models.ForeignKey('seguimiento.item')
	no_factura = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{1,20}$', 
				message='El numero de factura tiene de 1 a 20 cifras', 
				code='Numero Invalido'
			)
		]
	)
	no_autorizacion = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{5,20}$', 
				message='El numero de autorizacion tiene de 5 a 20 cifras', 
				code='Numero Invalido'
			)
		]
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	def totalItem(self):
		res = ingresoInsumos.objects.filter(item=self.item).aggregate(total=Sum('costo_total'))
		return res['total']
	def total(self):
		item = apps.get_model('seguimiento', 'item')
		res = ingresoInsumos.objects.filter(item__in=item.objects.filter(proyecto=self.item.proyecto)).aggregate(total=Sum('costo_total'))
		return res['total']
	def unitario(self):
		return round(self.costo_total/self.cantidad,3)
		
class salidaInsumos(models.Model):
	almacen = models.ForeignKey(almacen)
	insumos = models.ForeignKey(insumos)
	item = models.ForeignKey('seguimiento.item')
	confirmado = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)

#herraminetas
class herramientas(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	tipo = models.CharField(
		max_length=30,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def clean(self):
		aux = re.sub(' +',' ',self.decripcion)
		self.decripcion = aux.capitalize()
	def __str__(self):
		return self.decripcion

class herramientasAlmacen(models.Model):
	almacen = models.ForeignKey(almacen)
	herramientas = models.ForeignKey(herramientas)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	def stock(self):
		return ingresoHerramientas.objects.filter(almacen=self.almacen,herramientas=self.herramientas).aggregate(total=Sum('cantidad'))['total']
	class Meta:
		unique_together = (('almacen', 'herramientas'),)

class ingresoHerramientas(models.Model):
	almacen = models.ForeignKey(almacen)
	herramientas = models.ForeignKey(herramientas)
	proveedor = models.ForeignKey(proveedor)
	no_factura = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]{1,20}$', 
				message='El numero de factura tiene de 5 a 20 cifras', 
				code='Numero Invalido'
			)
		]
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)


class salidaHerramientas(models.Model):
	almacen = models.ForeignKey(almacen)
	herramientas = models.ForeignKey(herramientas)
	item = models.ForeignKey('seguimiento.item')
	debuelto = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
#maquinaria/equipo
class maquinaria_equipo(models.Model):
	decripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		unique=True
	)
	tipo = models.CharField(
		max_length=30,
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		null=True,
		blank=True,
	)
	def clean(self):
		aux = re.sub(' +',' ',self.decripcion)
		self.decripcion = aux.capitalize()
	def __str__(self):
		return self.decripcion

class maquinaria_equipoAlmacen(models.Model):
	almacen = models.ForeignKey(almacen)
	maquinaria_equipo = models.ForeignKey(maquinaria_equipo)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0
	)
	def stock(self):
		return ingresoMaquinaria_equipo.objects.filter(almacen=self.almacen,maquinaria_equipo=self.maquinaria_equipo).aggregate(total=Sum('cantidad'))['total']
	class Meta:
		unique_together = (('almacen', 'maquinaria_equipo'),)

class ingresoMaquinaria_equipo(models.Model):
	almacen = models.ForeignKey(almacen)
	maquinaria_equipo = models.ForeignKey(maquinaria_equipo)
	proveedor = models.ForeignKey(proveedor)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	costo_total = models.PositiveIntegerField(
		null=False,
		blank=False,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)


class salidaMaquinaria_equipo(models.Model):
	almacen = models.ForeignKey(almacen)
	maquinaria_equipo = models.ForeignKey(maquinaria_equipo)
	item = models.ForeignKey('seguimiento.item')
	debuelto = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	fecha =models.DateField(
		null=False,
		blank=False,
		auto_now=True
	)
	cantidad = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=0,
		validators=[MinValueValidator(1,"El valor no puede ser cero")]
	)

class tipoActivo(models.Model):
	tipo = models.CharField(
		max_length=60,
		blank=False,
		null=False,
		unique=True
	)
	anios_vida_util = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	observaciones = models.TextField(
		blank=True,
		null=True
	)
	
	def clean(self):
		aux = re.sub(' +',' ',self.tipo)
		self.tipo = aux.capitalize()
	def __str__(self):
		return self.tipo

class activo(models.Model):
	tipoActivo = models.ForeignKey(tipoActivo)
	descripcion = models.CharField(
		max_length=100,
		blank=False,
		null=False
	)
	marca = models.CharField(
		max_length=60,
		blank=False,
		null=False
	)
	modelo = models.CharField(
		max_length=60,
		blank=False,
		null=False
	)
	fecha_ingreso = models.DateField(
		blank=False,
		null=False
	)
	costo_total = models.FloatField(
		blank=False,
		null=False
	)
	def depreciasion(self):
		import datetime
		datenow = datetime.datetime.now()

		act = datenow.year - self.fecha_ingreso.year
		dep = self.costo_total / self.tipoActivo.anios_vida_util

		tdep = dep*act
		res= self.costo_total-tdep

		return res
	def __str__(self):
		return self.descripcion	"""