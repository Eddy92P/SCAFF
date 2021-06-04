# -*- coding: utf-8 -*-
from django.forms import ModelForm, modelformset_factory, inlineformset_factory
from django import forms
from activos_f.models import *
from dal import autocomplete
from django.core.exceptions import ValidationError

class Html5DateInput(forms.DateInput):
	input_type = 'date'

class crearPersonalAutAForm(forms.ModelForm):
	class Meta:
		model = personal_aut_act
		exclude = ['']
		widgets = {
			'personal':autocomplete.ModelSelect2(url='activos_f:personal_autocomplete'),
		}

    
crearPersonalFormSet = inlineformset_factory(Alta_baja_activo, Alta_baja_activo.personal.through, form=crearPersonalAutAForm, extra=2)
updatePersonalFormSet = inlineformset_factory(Alta_baja_activo, Alta_baja_activo.personal.through, form=crearPersonalAutAForm, extra=0)

class crearRubroForm(forms.ModelForm):
	class Meta:
		model = Rubro
		exclude = ['']
		labels = {
			'num_cuenta':'Cuenta Contable',
			'coeficiente':'Coeficiente de Depreciación',
			'vida_util':'Vida útil(años)'
		}
		widgets = {
			'num_cuenta':autocomplete.ModelSelect2(url='activos_f:asiento_autocomplete'),
		}

class crearTipo_bienForm(forms.ModelForm):
	class Meta:
		model = Tipo_bien
		exclude = ['']
		labels = {
			'tipo':'Descripción',
			'caracter':'Características'
		}
		widgets = {
			'rubro':autocomplete.ModelSelect2(url='activos_f:rubro_autocomplete'),
			'codigo':forms.HiddenInput()
		}

class crearUbicacionForm(ModelForm):
	class Meta:
		model = Ubicacion_gen
		exclude = ['']
		labels={
			'ubicacion_g':'Ubicación',
		}

class crearAltaActivoForm(forms.ModelForm):
	class Meta:
		model = Alta_baja_activo
		exclude = ['personal', 'baja', 'fecha_baja', 'razon_baja']
		labels = {
			'tipo_bien':'Tipo de Bien',
			'ubicacion':'Ubicación',
			'codigo':'Código',
			'tipo_alta':'Tipo de alta',
			'fecha_alta':'Fecha de alta',
			'valor_inic':'Valor inicial',
			'vida_util':'Vida útil(meses)',
			'vida_util_rest':'Vida útil restante(meses)',
			'estado_bien':'Estado del bien',
			'descripcion':'Descripción',
			'img_activo':'Imagen del activo',
			'vinculado':'Vinculado al proceso de produccion',
			'deprec':'Depreciación acumulada'
		}
		widgets = {
			'fecha_alta':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'tipo_bien':autocomplete.ModelSelect2(url='activos_f:tipo_bien_autocomplete'),
			'estado':forms.HiddenInput(),
			'codigo':forms.HiddenInput()
		}

class crearBajaActivoForm(forms.ModelForm):
	class Meta:
		model = Alta_baja_activo
		fields = ['fecha_baja', 'razon_baja', 'baja']
		widgets = {
			'fecha_baja':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
		}

class crearCapitalizacionForm(forms.ModelForm):
	class Meta:
		model = Capitalizacion
		exclude = ['']
		labels = {
			'tipo_bien':'Tipo de Bien',
			'fecha_cap':'Fecha de alta',
			'valor_inic':'Valor inicial'
		}
		widgets = {
			'fecha_cap':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'tipo_bien':autocomplete.ModelSelect2(url='activos_f:tipo_bien_autocomplete'),
			'estado':forms.HiddenInput()
		}
	def __init__(self, *args, **kwargs):
		super(crearCapitalizacionForm, self).__init__(*args, **kwargs)
		self.fields['alta_activo'].queryset = Alta_baja_activo.objects.filter(baja=False)

class reporteEspecBienForm(forms.Form):
	CHOICES = (('1','Vinculado'),('2','No Vinculado'))
	campo = forms.CharField(label="Fecha de Actualización/Depreciación", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo2 = forms.ChoiceField(label="Vinculado al proceso de producción", help_text="", choices=CHOICES)
	try:
		def __init__(self, *args, **kwargs):
			super(reporteEspecBienForm, self).__init__(*args, **kwargs)
			rubro = Rubro.objects.all().order_by('id').values_list('id', 'nombre')
			lista = list(rubro)
			lista.append(tuple(('T', 'Todo')))
			self.fields['campo1'].choices = lista
		campo1 = forms.ChoiceField(label="Rubro", help_text="", choices=lista)
	except Exception as e:
		campo1 = forms.ChoiceField(label="Rubro", help_text="")

class reporteAltaBajaForm(forms.Form):
	CHOICES = (('1', 'Altas'),('2', 'Bajas'))
	campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo3 = forms.ChoiceField(label="Alta/Baja", help_text="", choices=CHOICES)
	try:
		def __init__(self, *args, **kwargs):
			super(reporteAltaBajaForm, self).__init__(*args, **kwargs)
			rubro = Rubro.objects.all().order_by('id').values_list('id', 'nombre')
			lista = list(rubro)
			lista.append(tuple(('T', 'Todo')))
			self.fields['campo2'].choices = lista
		campo2 = forms.ChoiceField(label="Rubro", help_text="", choices=lista)
	except Exception as e:
		campo2 = forms.ChoiceField(label="Rubro", help_text="")

class reporteInventarioForm(forms.Form):
	campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))