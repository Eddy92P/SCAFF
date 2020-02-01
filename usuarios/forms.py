from django.forms import ModelForm
from django import forms
from usuarios.models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from django.urls import reverse

class Html5DateInput(forms.DateInput):
	input_type = 'date'

class crearKardexUsuarioForm(ModelForm):
	class Meta:
		model = kardex
		exclude = ['user']
		widgets ={
			'ci':forms.TextInput(attrs={'class':'form-control'}),
			'telefono_celular':forms.TextInput(attrs={'class':'form-control'}),
			'telefono_fijo':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'profesion':forms.TextInput(attrs={'class':'form-control'}),
			'cargo':forms.TextInput(attrs={'class':'form-control'})
		}
		labels = {
			'ci : C.I.'
		}

CHOICES = (('1','ID'),('2','Nombre'),)
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))
	buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)
class addPermissionsForm(forms.Form):
	mod_personal = forms.BooleanField(label="Otorgar permiso para el modulo usuarios", required=False)
	mod_contabilidad = forms.BooleanField(label="Otorgar permiso para el modulo contabilidad", required=False)
	mod_cargas = forms.BooleanField(label="Otorgar permiso para el modulo cargas", required=False)
class updateUsuarioUserForm(ModelForm):
	#email = forms.EmailField(required=True)
	class Meta:
		model=User
		fields=[
			#'username',
			'first_name',
			'last_name',
			'email',
		]
		widgets = {
			#'username':forms.TextInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(updateUsuarioUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True

class crearModificarKardexForm(ModelForm):
	class Meta:
		model = kardex
		fields = [		
			'telefono_fijo',
			'telefono_celular',
			'direccion',
		]
		widgets = {
			'telefono_fijo':forms.TextInput(attrs={'class':'form-control'}),
			'telefono_celular':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
		}
class crearUsuarioUserForm(UserCreationForm):
	class Meta:
		model = User
		fields =[
			'username',
			'first_name',
			'last_name',
			'email'
		]
		widgets ={
			'username':forms.TextInput(attrs={'class': 'form-control'}),
			'first_name':forms.TextInput(attrs={'class': 'form-control'}),
			'last_name':forms.TextInput(attrs={'class': 'form-control'}),
			'email':forms.EmailInput(attrs={'class': 'form-control'})
		}
	def __init__(self, *args, **kwargs):
		super(crearUsuarioUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
	


class cargoForm(ModelForm):
	class Meta:
		model = cargo
		exclude =['']

		
class darBajaForm(ModelForm):
	class Meta:
		model = User
		fields = [
			'is_active'
		]

class crearPersonalForm(ModelForm):
	class Meta:
		model = personal
		exclude = ['']
		widgets = {
			'fecha_ingreso':Html5DateInput(format='%Y-%m-%d'),
		}
		labels = {
			'ci':'CI',
			'ap_paterno':'Apellido Paterno',
			'ap_materno':'Apellido Materno',
		}