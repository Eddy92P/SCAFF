# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from import_export import resources
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from contabilidad.funciones import *

from django.db import models
from django.db.models import F
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Q

class nivel_uno(models.Model):
	descripcion = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo solo debe contener letras',
				code='Numero Invalido'
				)
			]
		)

	#Totales para balance general
	def debe_b_t(self, f1, f2):
		res = nivel_uno.objects.filter(id__lte=3, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_b_t(self, f1, f2):
		res = nivel_uno.objects.filter(id__lte=3, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def debe_d_t(self, f1, f2):
		res = nivel_uno.objects.filter(id__lte=3, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_d_t(self, f1, f2):
		res = nivel_uno.objects.filter(id__lte=3, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_b_t(self, f1, f2):
		res = nivel_uno.objects.filter(id__lte=3, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'] + self.saldo_b_ter(f1, f2))) + " CR"
		else:
			return res['total']

	def saldo_d_t(self, f1, f2):
		res = nivel_uno.objects.filter(id__lte=3, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'] + self.saldo_d_ter(f1, f2))) + " CR"
		else:
			return res['total']

	def suma_patrimonio_pasivo_bs(self, f1, f2):
		total_pasivo = nivel_uno.objects.filter(id=2, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b')))

		total_patrimonio = nivel_uno.objects.filter(id=3, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b')))

		if (total_pasivo is None) and (total_patrimonio is None):
			result = 0.0

		elif total_pasivo is None:
			result = total_patrimonio['total']

		elif total_patrimonio is None:
			result = total_pasivo['total']

		else:
			result = total_pasivo['total'] + total_patrimonio['total']

		if result < 0:
			return str(abs(result)) + " CR"
		else:
			return result

	def suma_patrimonio_pasivo_dls(self, f1, f2):
		total_pasivo = nivel_uno.objects.filter(id=2, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d')))

		total_patrimonio = nivel_uno.objects.filter(id=3, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d')))

		if (total_pasivo is None) and (total_patrimonio is None):
			result = 0.0

		elif total_pasivo is None:
			result = total_patrimonio['total']

		elif total_patrimonio is None:
			result = total_pasivo['total']

		else:
			result = total_pasivo['total'] + total_patrimonio['total']

		if result < 0:
			return str(abs(result)) + " CR"
		else:
			return result


	#Totales para estado de resultados
	def debe_b_ter(self, f1, f2):
		res = nivel_uno.objects.filter(id__gte=4, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_b_ter(self, f1, f2):
		res = nivel_uno.objects.filter(id__gte=4, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def debe_d_ter(self, f1, f2):
		res = nivel_uno.objects.filter(id__gte=4, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_d_ter(self, f1, f2):
		res = nivel_uno.objects.filter(id__gte=4, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_b_ter(self, f1, f2):
		res = nivel_uno.objects.filter(id__gte=4, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b')))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_d_ter(self, f1, f2):
		res = nivel_uno.objects.filter(id__gte=4, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d')))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def mostrar_saldo_b_ter(self, f1, f2):
		res = nivel_uno.objects.filter(id__gte=4, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

	def mostrar_saldo_d_ter(self, f1, f2):
		res = nivel_uno.objects.filter(id__gte=4, nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

	def utilidad_bs(self, f1, f2):
		res = self.debe_b_ter

	def __unicode__(self):
		return str(self.id) + " " + self.descripcion

	#Totales para sumas y saldos
	"""def debe_b_ts(self):
		res = nivel_uno.objects.aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b'))
		return res['total']

	def haber_b_ts(self):
		res = nivel_uno.objects.aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b'))
		return res['total']

	def debe_d_ts(self):
		res = nivel_uno.objects.aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d'))
		return res['total']

	def haber_d_ts(self):
		res = nivel_uno.objects.aggregate(total=Sum('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d'))
		return res['total']

	def saldo_b_ts(self):
		res = nivel_uno.objects.aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b')))
		return res['total']

	def saldo_d_ts(self):
		res = nivel_uno.objects.aggregate(total=Sum(F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d') - F('nivel_dos__nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d')))
		return res['total']"""

class nivel_dos(models.Model):
	nivel_uno = models.ForeignKey(nivel_uno, on_delete=models.CASCADE)
	codigo = models.CharField(
		max_length=2,
		null=False,
		blank=False,
		default="",
		validators=[
			RegexValidator(
				regex=r'^[0-9]+$',
				message='El campo debe contener solo números',
				code='Numero Invalido'
				)
			]
		)
	descripcion = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo solo debe contener letras',
				code='Numero Invalido'
				)
			]
		)

	def __unicode__(self):
		return self.codigo + " " + self.descripcion

	def debe_b_t(self, f1, f2):
		res = nivel_dos.objects.filter(nivel_uno=self.nivel_uno, nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_b_t(self, f1, f2):
		res = nivel_dos.objects.filter(nivel_uno=self.nivel_uno, nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def debe_d_t(self, f1, f2):
		res = nivel_dos.objects.filter(nivel_uno=self.nivel_uno, nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_d_t(self, f1, f2):
		res = nivel_dos.objects.filter(nivel_uno=self.nivel_uno, nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_b_t(self, f1, f2):
		res = nivel_dos.objects.filter(nivel_uno=self.nivel_uno, nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_b') - F('nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_b')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

	def saldo_d_t(self, f1, f2):
		res = nivel_dos.objects.filter(nivel_uno=self.nivel_uno, nivel_tres__nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_tres__nivel_cuatro__nivel_cinco__asiento__debe_d') - F('nivel_tres__nivel_cuatro__nivel_cinco__asiento__haber_d')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']


class nivel_tres(models.Model):
	nivel_uno = models.ForeignKey(nivel_uno, on_delete=models.CASCADE)
	nivel_dos = models.ForeignKey(nivel_dos, on_delete=models.CASCADE)
	codigo = models.CharField(
		max_length=4,
		null=False,
		blank=False,
		default="",
		validators=[
			RegexValidator(
				regex=r'^[0-9]+$',
				message='El campo debe contener solo números',
				code='Numero Invalido'
				)
			]
		)
	descripcion = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo solo debe contener letras',
				code='Numero Invalido'
				)
			]
		)

	def __unicode__(self):
		return self.codigo + " " + self.descripcion

	def debe_b_t(self, f1, f2):
		res = nivel_tres.objects.filter(nivel_dos=self.nivel_dos, nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_cuatro__nivel_cinco__asiento__debe_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_b_t(self, f1, f2):
		res = nivel_tres.objects.filter(nivel_dos=self.nivel_dos, nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_cuatro__nivel_cinco__asiento__haber_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def debe_d_t(self, f1, f2):
		res = nivel_tres.objects.filter(nivel_dos=self.nivel_dos, nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_cuatro__nivel_cinco__asiento__debe_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_d_t(self, f1, f2):
		res = nivel_tres.objects.filter(nivel_dos=self.nivel_dos, nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_cuatro__nivel_cinco__asiento__haber_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_b_t(self, f1, f2):
		res = nivel_tres.objects.filter(nivel_dos=self.nivel_dos, nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_cuatro__nivel_cinco__asiento__debe_b') - F('nivel_cuatro__nivel_cinco__asiento__haber_b')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

	def saldo_d_t(self, f1, f2):
		res = nivel_tres.objects.filter(nivel_dos=self.nivel_dos, nivel_cuatro__nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_cuatro__nivel_cinco__asiento__debe_d') - F('nivel_cuatro__nivel_cinco__asiento__haber_d')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']


class nivel_cuatro(models.Model):
	nivel_uno = models.ForeignKey(nivel_uno, on_delete=models.CASCADE)
	nivel_dos = models.ForeignKey(nivel_dos, on_delete=models.CASCADE)
	nivel_tres = models.ForeignKey(nivel_tres, on_delete=models.CASCADE)
	codigo = models.CharField(
		max_length=6,
		null=False,
		blank=True,
		default="",
		validators=[
			RegexValidator(
				regex=r'^[0-9]+$',
				message='El campo debe contener solo números',
				code='Numero Invalido'
				)
			]
		)
	descripcion = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo solo debe contener letras',
				code='Numero Invalido'
				)
			]
		)

	def __unicode__(self):
		return self.codigo + " " + self.descripcion

	def debe_b_t(self, f1, f2):
		res = nivel_cuatro.objects.filter(nivel_tres=self.nivel_tres, nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_cinco__asiento__debe_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_b_t(self, f1, f2):
		res = nivel_cuatro.objects.filter(nivel_tres=self.nivel_tres, nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_cinco__asiento__haber_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def debe_d_t(self, f1, f2):
		res = nivel_cuatro.objects.filter(nivel_tres=self.nivel_tres, nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_cinco__asiento__debe_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_d_t(self, f1, f2):
		res = nivel_cuatro.objects.filter(nivel_tres=self.nivel_tres, nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('nivel_cinco__asiento__haber_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_b_t(self, f1, f2):
		res = nivel_cuatro.objects.filter(nivel_tres=self.nivel_tres, nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_cinco__asiento__debe_b') - F('nivel_cinco__asiento__haber_b')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

	def saldo_d_t(self, f1, f2):
		res = nivel_cuatro.objects.filter(nivel_tres=self.nivel_tres, nivel_cinco__asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('nivel_cinco__asiento__debe_d') - F('nivel_cinco__asiento__haber_d')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

class nivel_cinco(models.Model):
	nivel_uno = models.ForeignKey(nivel_uno, on_delete=models.CASCADE)
	nivel_dos = models.ForeignKey(nivel_dos, on_delete=models.CASCADE)
	nivel_tres = models.ForeignKey(nivel_tres, on_delete=models.CASCADE)
	nivel_cuatro = models.ForeignKey(nivel_cuatro, on_delete=models.CASCADE)
	codigo = models.CharField(
		max_length=10,
		null=False,
		blank=True,
		default="",
		validators=[
			RegexValidator(
				regex=r'^[0-9]+$',
				message='El campo debe contener solo números',
				code='Numero Invalido'
				)
			]
		)
	descripcion = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo solo debe contener letras',
				code='Numero Invalido'
				)
			]
		)
	moneda = models.CharField(
		max_length=2,
		null=False,
		blank=False,
		choices=(('1','Bs.'),('2','$us.'))
		)
	def __unicode__(self):
		return self.codigo + " " + self.descripcion

	def debe_b_t(self, f1, f2):
		res = nivel_cinco.objects.filter(nivel_cuatro=self.nivel_cuatro, asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('asiento__debe_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_b_t(self, f1, f2):
		res = nivel_cinco.objects.filter(nivel_cuatro=self.nivel_cuatro, asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('asiento__haber_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def debe_d_t(self, f1, f2):
		res = nivel_cinco.objects.filter(nivel_cuatro=self.nivel_cuatro, asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('asiento__debe_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_d_t(self, f1, f2):
		res = nivel_cinco.objects.filter(nivel_cuatro=self.nivel_cuatro, asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('asiento__haber_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_b_t(self, f1, f2):
		res = nivel_cinco.objects.filter(nivel_cuatro=self.nivel_cuatro, asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('asiento__debe_b') - F('asiento__haber_b')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

	def saldo_d_t(self, f1, f2):
		res = nivel_cinco.objects.filter(nivel_cuatro=self.nivel_cuatro, asiento__encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('asiento__debe_d') - F('asiento__haber_d')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

class encabezadoas(models.Model):
	cotizacion = models.FloatField(
		null=False,
		default=0
		)
	numero_comp = models.PositiveIntegerField(
		blank=True,
		default=0
		)
	fecha = models.DateField(
		null=False,
		blank=False
		)
	moneda = models.CharField(
		max_length=4,
		null=False,
		blank=False,
		choices=(('1','Bs.'),('2','$us'))
			)
	tipo_trans = models.CharField(
		max_length=1,
		null=False,
		blank=False,
		choices=(('E','EGRESO'),('I','INGRESO'),('T','TRASPASO'),('A','AJUSTE'))
		)
	glosa = models.CharField(
		max_length=650,
		blank=True
		)
	entregado = models.CharField(
		max_length=60,
		null=False,
		blank=False,
		)
	debe_bs = models.DecimalField(
		max_digits=15,
		decimal_places=2
		)
	haber_bs = models.DecimalField(
		max_digits=15,
		decimal_places=2
		)
	debe_dls = models.DecimalField(
		max_digits=15,
		decimal_places=2
		)
	haber_dls = models.DecimalField(
		max_digits=15,
		decimal_places=2
		)
	dif_bs = models.DecimalField(
		max_digits=15,
		decimal_places=2
		)
	dif_dls = models.DecimalField(
		max_digits=15,
		decimal_places=2
		)

	class Meta:
		unique_together = (('numero_comp','tipo_trans'))

	def save_related(self, request, form, formsets, change):
    		super(encabezadoas, self).save_related(request, form, formsets, change)
      		encabezadoas = encabezadoas.objects.get(pk=1)
      		form.instance.encabezadoas.add(encabezadoas)

	def fecha_f(self):
		return self.fecha.strftime("%d/%m/%y")

	def fecha_fi(self):
		return self.fecha.strftime("%d/%m/%Y")

	def encabezado(self):
		fecha = self.fecha.strftime('%d%m')
		trans = self.tipo_trans
		comp = self.numero_comp
		res = trans + '-' + fecha + str(comp)
		return res

	def letras(self):
		res = numero_to_letras(self.debe_bs)
		return res

	def letras2(self):
		res = numero_to_letras(self.debe_dls)
		return res


class asiento(models.Model):
	encabezadoas = models.ForeignKey(encabezadoas, related_name="asientos", on_delete=models.CASCADE)
	nivel_cinco = models.ForeignKey(nivel_cinco)
	refer = models.CharField(
		max_length=200,
		null=False,
		blank=False
		)
	debe_b = models.DecimalField(
		default=0,
		max_digits=15,
		decimal_places=2,
		null=True,
		blank=True
		)
	haber_b = models.DecimalField(
		default=0,
		max_digits=15,
		decimal_places=2,
		null=True,
		blank=True
		)
	debe_d = models.DecimalField(
		default=0,
		max_digits=15,
		decimal_places=2,
		null=True,
		blank=True
		)
	haber_d = models.DecimalField(
		default=0,
		max_digits=15,
		decimal_places=2,
		null=True,
		blank=True
		)
	banco = models.CharField(
		max_length=3,
		blank=True,
		choices=(('D','Depósito'),('I','Intereses Percibidos'),('O','Giros'),('G','Girado'),('R','Retiro'),('P','Intereses Pagados'),('B','Gastos Bancarios'),('S','Débito Cuenta'))
		)
	numero_cheque = models.CharField(
		max_length=15,
		blank=True
		)
	opciones_p = models.CharField(
		max_length=1,
		blank=True,
		choices=(('R','Retenido'),('A','Asumido'),('F','Factura'),('D','Descuento'))
		) 
	opciones_s = models.CharField(
		max_length=4,
		blank=True,
		choices=(('C','IU Compras'),('S','IU Servicio'),('RC','RC-IVA'),('A','Alquileres'),('Comp','Compras'),('B','Boletos'),('I','Importaciones'),('G','Gasolina'),('V','Ventas'),('SC','Sin Derecho a Crédito Fiscal'))
		)
	auxiliar = models.PositiveIntegerField(
		null=True,
		blank=True
		)
	auxiliar_s = models.DecimalField(
		null=True,
		blank=True,
		default=0,
		max_digits=15,
		decimal_places=2
		)

	class Meta:
		ordering = ['id', 'auxiliar', '-nivel_cinco__nivel_cuatro']

	def suma(self):
		res = self.debe_b - self.haber_b
		return res

	def debe_b_t(self, f1, f2):
		res = asiento.objects.filter(nivel_cinco=self.nivel_cinco, encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('debe_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_b_t(self, f1, f2):
		res = asiento.objects.filter(nivel_cinco=self.nivel_cinco, encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('haber_b'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def debe_d_t(self, f1, f2):
		res = asiento.objects.filter(nivel_cinco=self.nivel_cinco, encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('debe_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def haber_d_t(self, f1, f2):
		res = asiento.objects.filter(nivel_cinco=self.nivel_cinco, encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum('haber_d'))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_b_t_p(self, f1, f2):
		res = asiento.objects.filter(nivel_cinco=self.nivel_cinco, encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('haber_b') - F('debe_b')))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_d_t_p(self, f1, f2):
		res = asiento.objects.filter(nivel_cinco=self.nivel_cinco, encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('haber_d') - F('debe_d')))
		if res['total'] == None:
			return 0.0
		else:
			return res['total']

	def saldo_b_t(self, f1, f2):
		res = asiento.objects.filter(nivel_cinco=self.nivel_cinco, encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('debe_b') - F('haber_b')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']

	def saldo_d_t(self, f1, f2):
		res = asiento.objects.filter(nivel_cinco=self.nivel_cinco, encabezadoas__fecha__range=(f1, f2)).aggregate(total=Sum(F('debe_d') - F('haber_d')))
		if res['total'] == None:
			return 0.0
		elif res['total'] < 0:
			return str(abs(res['total'])) + " CR"
		else:
			return res['total']


class Factura(models.Model):
	asiento = models.OneToOneField(asiento)
	sucursal = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		default="Oficina Central(Potosí)"
		)
	fecha_fac = models.DateField(
		null=False,
		blank=False
		)
	nit_prov = models.CharField(
		max_length=13,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	nomb_razon = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener letras y números',
				code='Numero Invalido')
			]
		)
	nro_fact = models.CharField(
		max_length=20,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	nro_dui = models.CharField(
		max_length=30,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener números y letras',
				code='Numero Invalido')
			]
		)
	nro_aut = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener números y letras',
				code='Numero Invalido')
			]
		)
	importe_fac = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	importe_credit = models.FloatField(
		blank=True,
		default=0
		)
	subtot = models.FloatField(
		blank=True,
		default=0
		)
	descuento = models.FloatField(
		blank=True,
		default=0
		)
	base_credito = models.FloatField(
		blank=True,
		default=0
		)
	credit_fisc = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	cod_cont = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener números y letras',
				code='Numero Invalido')
			]
		)
	tipo_fac = models.CharField(
		max_length=1,
		null=False,
		blank=False,
		choices=(('1','Compras para mercado interno con destino a actividades gravadas'),('2','Compras para mercado interno con destino a actividades no gravadas'),('3','Compras sujetas a proporcionalidad'),('4','Compras para exportaciones'),('5','Compras tanto para el mercado interno como para exportaciones'))
		)
	estado = models.BooleanField(
		default=False
		)

	def fecha_f(self):
		return self.fecha_fac.strftime("%d/%m/%y")

	def codigo(self):
		cod = self.cod_cont
		aux = 0
		aux1 = 0
		aux2 = 2
		res = ""
		res2 = len(cod)/2
		while(aux<res2):
			res1 = cod[aux1:aux2]
			res = res + res1 + "-"
			aux1 += 2
			aux2 += 2
			aux += 1
		res = res[:len(res)-1]
		return res

	def save_related(self, request, form, formsets, change):
		super(Factura, self).save_related(request, form, formsets, change)
		Factura = Factura.objects.get(pk=1)
		form.instance.Factura.add(Factura)

class Factura_V(models.Model):
	asiento = models.OneToOneField(asiento)
	sucursal = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		default="Oficina Central(Potosí)"
		)
	fecha_fac = models.DateField(
		null=False,
		blank=False
		)
	nro_fact = models.CharField(
		max_length=20,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	nro_aut = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener números y letras',
				code='Numero Invalido')
			]
		)
	estado_p = models.CharField(
		max_length=1,
		null=False,
		blank=False,
		choices=(('A','Anulada'),('V','Valida'),('E','Extraviada'),('N','No utilizada'),('C','Emitida en contingencia')))
	nit_cliente = models.CharField(
		max_length=13,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	nomb_razon = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener letras y números',
				code='Numero Invalido')
			]
		)
	importe_fac = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	importe_ice = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	export_oper = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	ventas_grav = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	subtot = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	descuento = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	base_debito = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	debito_fisc = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	cod_cont = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener números y letras',
				code='Numero Invalido')
			]
		)
	estado = models.BooleanField(
		default=False
		)

	def fecha_f(self):
		return self.fecha_fac.strftime("%d/%m/%y")

	def codigo(self):
		cod = self.cod_cont
		aux = 0
		aux1 = 0
		aux2 = 2
		res = ""
		res2 = len(cod)/2
		while(aux<res2):
			res1 = cod[aux1:aux2]
			res = res + res1 + "-"
			aux1 += 2
			aux2 += 2
			aux += 1
		res = res[:len(res)-1]
		return res

class Cotizacion(models.Model):
	fecha = models.DateField(
		null=False,
		blank=False
		)
	tipo_c = models.FloatField(
		null=False,
		blank=False
		)
	ufv = models.DecimalField(
		null=False,
		blank=False,
		default=0,
		max_digits=6,
		decimal_places=5
		)

	def fecha_f(self):
		return self.fecha.strftime("%d/%m/%y")

	def __unicode__(self):
		return str(self.fecha_f()) + " " + "T/C:" + str(self.tipo_c) + " " + "/" + " " + "UFV:" + str(self.ufv)

class Proyecto(models.Model):
	codigo = models.CharField(
		max_length=5,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo debe tener sólo números',
				code='Numero Invalido'
				)
			]
		)
	nombre = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe contener letras',
				code='Numero Invalido',
				)
			]
		)

	def __str__(self):
		return self.nombre

class bancarizacion(models.Model):
	factura = models.OneToOneField(Factura)
	modalidad = models.CharField(
		max_length=10,
		null=False,
		blank=False,
		default='1',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo sólo permite números',
				code='Numero Invalido',
				)
			]
		)
	numero_contr = models.CharField(
		max_length=30,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo sólo permite números',
				code='Numero Invalido',
				)
			]
		)
	num_cuenta_doc = models.CharField(
		max_length=40,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo sólo permite números',
				code='Numero Invalido',
				)
			]
		)
	importe = models.DecimalField(
		null=False,
		blank=False,
		default=0,
		max_digits=20,
		decimal_places=2
		)
	monto_acum = models.DecimalField(
		null=False,
		blank=False,
		default=0,
		max_digits=20,
		decimal_places=2
		)
	nit_entidad = models.CharField(
		max_length=30,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo sólo permite números',
				code='Numero Invalido',
				)
			]
		)
	num_trans = models.CharField(
		max_length=30,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo sólo permite números',
				code='Numero Invalido',
				)
			]
		)
	tipo_docum = models.CharField(
		max_length=2,
		null=False,
		blank=False,
		choices=(('1','Cheques'),('2','Ordenes de Transferencia'),('3','Ordenes de Transferencia Electrónica de Fondos'),('4','Transferencia de Fondos'),('5','Voucher de Tarjeta de Débito'),('6','Voucher de Tarjeta de Crédito'),('7','Tarjetas Pre-Pagadas'),('8','Boletas de Déposito de Cuenta'),('9','Cartas de Crédito'),('10','Otros'))
		)
	fecha = models.DateField(
		null=False,
		blank=False
		)
	estado = models.BooleanField(
		default = False
		)



























































































"""class Factura_boleto(models.Model):
	asiento = models.OneToOneField(asiento)
	sucursal = models.CharField(
		max_length=60,
		null=False,
		blank=False,
		default="Oficina Central(Potosí)"
		)
	fecha_fac = models.DateField(
		null=False,
		blank=False
		)
	nit_linea = models.CharField(
		max_length=13,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	nomb_razon = models.CharField(
		max_length=80,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo solo debe contener letras',
				code='Numero Invalido')
			]
		)
	nro_boleto = models.CharField(
		max_length=30,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	nro_dui = models.CharField(
		max_length=1,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	nro_aut = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		default='1',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	importe_boleto = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	importe_credit = models.FloatField(
		blank=True,
		default=0
		)
	subtot = models.FloatField(
		blank=True,
		default=0
		)
	descuento = models.FloatField(
		blank=True,
		default=0
		)
	base_credito = models.FloatField(
		blank=True,
		default=0
		)
	credit_fisc = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	cod_cont = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener números y letras',
				code='Numero Invalido')
			]
		)
	tipo_fac = models.CharField(
		max_length=1,
		null=False,
		blank=False,
		choices=(('1','Compras para mercado interno con destino a actividades gravadas'),('2','Compras para mercado interno con destino a actividades no gravadas'),('3','Compras sujetas a proporcionalidad'),('4','Compras para exportaciones'),('5','Compras tanto para el mercado interno como para exportaciones'))
		)

class Factura_import(models.Model):
	asiento = models.OneToOneField(asiento)
	sucursal = models.CharField(
		max_length=60,
		null=False,
		blank=False,
		default="Oficina Central(Potosí)"
		)
	fecha = models.DateField(
		null=False,
		blank=False
		)
	nit_prov = models.CharField(
		max_length=13,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	nomb_razon = models.CharField(
		max_length=80,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo solo debe contener letras',
				code='Numero Invalido')
			]
		)
	nro_fact = models.CharField(
		max_length=30,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	cod_aduana = models.CharField(
		max_length=3,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe tener números',
				code='Numero Invalido'
				)
			]
		)
	tipo_tram = models.CharField(
		max_length=1,
		null=False,
		blank=False,
		default='C',
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]',
				message='El campo sólo debe tener letras',
				code='Numero Invalido'
				)
			]
		)
	nro_tramite = models.CharField(
		max_length=4,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo sólo debe tener números',
				code='Numero Invalido'
				)
			]
		)
	nro_dui = models.CharField(
		max_length=20,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener números y letras',
				code='Numero Invalido')
			]
		)
	nro_aut = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		default='3',
		validators=[
			RegexValidator(
				regex=r'^[0-9]',
				message='El campo solo debe contener números',
				code='Numero Invalido')
			]
		)
	importe_fac = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	importe_credit = models.FloatField(
		blank=True,
		default=0
		)
	subtot = models.FloatField(
		blank=True,
		default=0
		)
	descuento = models.FloatField(
		blank=True,
		default=0
		)
	base_credito = models.FloatField(
		blank=True,
		default=0
		)
	credit_fisc = models.FloatField(
		null=False,
		blank=False,
		default=0
		)
	cod_cont = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		default='0',
		validators=[
			RegexValidator(
				regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]',
				message='El campo solo debe contener números y letras',
				code='Numero Invalido')
			]
		)
	tipo_fac = models.CharField(
		max_length=1,
		null=False,
		blank=False,
		choices=(('1','Compras para mercado interno con destino a actividades gravadas'),('2','Compras para mercado interno con destino a actividades no gravadas'),('3','Compras sujetas a proporcionalidad'),('4','Compras para exportaciones'),('5','Compras tanto para el mercado interno como para exportaciones'))
		)"""