# -*- coding: utf-8 -*-
from django.forms import ModelForm, modelformset_factory, inlineformset_factory
from django import forms
from almacenes.models import *
from dal import autocomplete

class Html5DateInput(forms.DateInput):
	input_type = 'date'

class crearProveedorForm(ModelForm):
	class Meta:
		model = proveedor
		exclude = ['']
		labels={
			'nombre':'Nombre Completo',
			'telefono':'Teléfono',
			'nit':'NIT',
			'email':'E-Mail',
			'direccion':'Dirección'
		}

class crearClienteForm(ModelForm):
	class Meta:
		model = cliente
		exclude = ['']
		labels = {
			'num_cuenta':'Cuenta Contabilidad',
			'ubicacion_gen':'Ubicación'
		}
		widgets = {
			'ubicacion_gen':autocomplete.ModelSelect2(url='almacenes:ubicacion_autocomplete'),
			'num_cuenta':autocomplete.ModelSelect2(url='almacenes:asiento_autocomplete'),
		} 

class crearTipoEntradaForm(ModelForm):
	class Meta:
		model = tipo_entrada
		exclude = ['']

class crearTipoSalidaForm(ModelForm):
	class Meta:
		model = tipo_salida
		exclude = ['']

class crearUnidadForm(ModelForm):
	class Meta:
		model = unidad
		exclude = ['']

#material
class crearCategoriaForm(ModelForm):
	class Meta:
		model = categoria
		exclude = ['']
		labels = {
			'num_cuenta':'Cuenta Contabilidad',
		}
		widgets = {
			'almacen':autocomplete.ModelSelect2(url='almacenes:almacen_autocomplete'),
			'num_cuenta':autocomplete.ModelSelect2(url='almacenes:asiento_autocomplete'),
		} 

class crearSubCategoriaForm(ModelForm):
	class Meta:
		model = subcategoria
		exclude = ['']
		
		widgets = {
			'almacen':autocomplete.ModelSelect2(url='almacenes:almacen_autocomplete'),
			'categoria':autocomplete.ModelSelect2(url='almacenes:categoria_autocomplete', forward=['almacen']),
			'codigo':forms.HiddenInput(),
		} 
	

class crearItemForm(ModelForm):
	class Meta:
		model = item
		exclude = ['']
		widgets = {
			'almacen':autocomplete.ModelSelect2(url='almacenes:almacen_autocomplete'),
			'categoria':autocomplete.ModelSelect2(url='almacenes:categoria_autocomplete', forward=['almacen']),
			'subcategoria':autocomplete.ModelSelect2(url='almacenes:subcategoria_autocomplete', forward=['categoria']),
		}
		labels = {
			'activo_f':'Activo Fijo'
		}

class crearItemActForm(ModelForm):
	class Meta:
		model = item_act
		exclude = ['']
		widgets = {
			'item':autocomplete.ModelSelect2(url='almacenes:item_act_autocomplete'),
		}
		labels = {
			'activo_f':'Activo Fijo'
		}
	def __init__(self, *args, **kwargs):
		super(crearItemActForm, self).__init__(*args, **kwargs)
		self.fields['item'].queryset = item.objects.filter(activo_f=True)

class crearEncabezadoIngresoForm(forms.ModelForm):
	class Meta:
		model = encingresoitem
		exclude = ['personal']
		widgets = {
			'fecha':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'tipo_entrada':forms.Select(attrs={'class':'form-control'}),
			'proveedor':forms.Select(attrs={'class':'form-control'}),
			'factura':forms.TextInput(attrs={'class':'form-control'}),
			'concepto':forms.TextInput(attrs={'class':'form-control'}),
			'iva':forms.CheckboxInput(),
			'total':forms.TextInput(attrs={'class':'form-control'}),
			'total_iva':forms.TextInput(attrs={'class':'form-control'}),
			'importe_iva':forms.TextInput(attrs={'class':'form-control'}),
			'proveedor':autocomplete.ModelSelect2(url='almacenes:proveedor_autocomplete'),
			'cerrado':forms.HiddenInput()
		}

class crearIngresoItemForm(forms.ModelForm):
	class Meta:
		model = ingresoitem
		exclude = ['']
		widgets = {
			'item':autocomplete.ModelSelect2(url='almacenes:item_autocomplete'),
			}

	def __init__(self, *args, **kwargs):
		super(crearIngresoItemForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
				self.fields[field].widget.attrs.update({
		    		'class': 'form-control'
		})
    

crearIngresoItemFormSet = inlineformset_factory(encingresoitem, ingresoitem, form=crearIngresoItemForm, extra=1, min_num=1, validate_min=True)
updateIngresoItemFormSet = inlineformset_factory(encingresoitem, ingresoitem, form=crearIngresoItemForm, extra=1)


class crearPersonalAutForm(forms.ModelForm):
	class Meta:
		model = personal_aut
		exclude = ['']
		widgets = {	
			'personal':autocomplete.ModelSelect2(url='almacenes:personal_autocomplete'),
		}

    
crearPersonalFormSet = inlineformset_factory(encingresoitem, encingresoitem.personal.through, form=crearPersonalAutForm, extra=2)
updatePersonalFormSet = inlineformset_factory(encingresoitem, encingresoitem.personal.through, form=crearPersonalAutForm, extra=0)

class crearPersonalSForm(forms.ModelForm):
	class Meta:
		model = personal_aut_s
		exclude = ['']
		widgets = {
			'personal':autocomplete.ModelSelect2(url='almacenes:personal_autocomplete'),
		}

crearPersonalSFormSet = inlineformset_factory(encsalidaitem, encsalidaitem.personal.through, form=crearPersonalSForm, extra=2)
updatePersonalSFormSet = inlineformset_factory(encsalidaitem, encsalidaitem.personal.through, form=crearPersonalSForm, extra=0)

class crearEncabezadoSalidaForm(forms.ModelForm):
	class Meta:
		model = encsalidaitem
		exclude = ['personal']
		widgets = {
			'fecha':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'nro_comp':forms.TextInput(attrs={'class':'form-control'}),
			'seccion':forms.TextInput(attrs={'class':'form-control'}),
			'concepto':forms.TextInput(attrs={'class':'form-control'}),
			'tipo_salida':forms.Select(attrs={'class':'form-control'}),
			'cliente':autocomplete.ModelSelect2(url='almacenes:cliente_autocomplete'),
			'cerrado':forms.HiddenInput()
		}
		labels = {
			'nro_comp':'Número de Comprobante',
			'cliente':'Destino(Cliente)'
		}

class crearSalidaItemForm(forms.ModelForm):
	class Meta:
		model = salidaitem
		exclude = ['']
		widgets = {
			'item':autocomplete.ModelSelect2(url='almacenes:item_autocomplete')
		}
		
	def __init__(self, *args, **kwargs):
		super(crearSalidaItemForm, self).__init__(*args, **kwargs)
		self.fields['costo_unit'].widget.attrs['readonly'] = True
		self.fields['sub_total'].widget.attrs['readonly'] = True
		for field in iter(self.fields):
				self.fields[field].widget.attrs.update({'class': 'form-control'})
    

crearSalidaItemFormSet = inlineformset_factory(encsalidaitem, salidaitem, form=crearSalidaItemForm, extra=1)



CHOICES = (('1', 'Nombre'), ('2', 'ID'))
class searchForm(forms.Form):
	search = forms.IntegerField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))
	buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)


class repGeneralForm(forms.Form):
	try:
		almacenes = categoria.objects.all().order_by('id').values_list('id', 'nombre')
		lista = list(almacenes)
		lista.append(tuple(('T','Todo')))
		campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo2 = forms.ChoiceField(label="Almacen", help_text="", choices=lista)
	except Exception as e:
		campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo2 = forms.ChoiceField(label="Almacen", help_text="")

class reporteDiarioEForm(forms.Form):
	campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))

class reporteResKardexForm(forms.Form):
	campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))

class repResumenEySForm(forms.Form):
	CHOICES = (('E', 'Entrada'), ('S', 'Salida'))
	campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo2 = forms.ChoiceField(label="Tipo de Movimiento", help_text="", choices=CHOICES)

class repDetalleEntradasForm(forms.Form):
	CHOICES = (('T', 'Tipo de Entrada'), ('S', 'Sub Categoria'))
	campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo2 = forms.ChoiceField(label="Filtrado por", help_text="", choices=CHOICES)

class repDetalleSalidasForm(forms.Form):
	CHOICES = (('T', 'Tipo de Salida'), ('S', 'Sub Categoria'))
	campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo2 = forms.ChoiceField(label="Filtrado por", help_text="", choices=CHOICES)

class repDetalleClienteForm(forms.Form):
	try:
		clientes = cliente.objects.all().order_by('id').values_list('id', 'nombre')
		lista = list(clientes)
		lista.append(tuple(('T','Todo')))
		campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo2 = forms.ChoiceField(label="Cliente", help_text="", choices=lista)
	except Exception as e:
		campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo2 = forms.ChoiceField(label="Cliente", help_text="")

class repDetalleProveedorForm(forms.Form):
	try:
		proveedores = proveedor.objects.all().order_by('id').values_list('id', 'nombre')
		lista = list(proveedores)
		lista.append(tuple(('T','Todo')))
		campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo2 = forms.ChoiceField(label="Proveedor", help_text="", choices=lista)
	except Exception as e:
		campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo2 = forms.ChoiceField(label="Proveedor", help_text="")

class actualizarInventarioForm(forms.Form):
	campo = forms.CharField(label="Fecha de Actualización", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))

class repKardexValForm(forms.Form):
	try:
		items = item.objects.all().order_by('nombre').values_list('id', 'nombre')
		lista = list(items)
		campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo2 = forms.ChoiceField(label="Item", help_text="", choices=lista)
	except Exception as e:
		campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
		campo2 = forms.ChoiceField(label="Item", help_text="")