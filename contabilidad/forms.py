# -*- coding: utf-8 -*-
from django.forms import ModelForm, modelformset_factory, inlineformset_factory
from django import forms
from contabilidad.models import *
from dal import autocomplete
import os


class Html5DateInput(forms.DateInput):
	input_type = 'date'

class crearEncabezadoForm(forms.ModelForm):
	class Meta:
		model = encabezadoas
		exclude = [""]
		widgets = {
			'fecha':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'glosa':forms.Textarea(attrs={'class':'form-control', 'cols':2, 'rows':1}),
			'numero_comp':forms.TextInput(attrs={'class':'form-control'}),
			'cotizacion':forms.TextInput(attrs={'class':'form-control'}),
			'moneda':forms.Select(attrs={'class':'form-control'}),
			'tipo_trans':forms.Select(attrs={'class':'form-control'}),
			'entregado':forms.TextInput(attrs={'class':'form-control'}),
			'debe_bs':forms.TextInput(attrs={'class':'form-control'}),
			'haber_bs':forms.TextInput(attrs={'class':'form-control'}),
			'debe_dls':forms.TextInput(attrs={'class':'form-control'}),
			'haber_dls':forms.TextInput(attrs={'class':'form-control'}),
			'dif_bs':forms.TextInput(attrs={'class':'form-control'}),
			'dif_dls':forms.TextInput(attrs={'class':'form-control'}),
			'cerrado':forms.HiddenInput(),
			}
		labels = {
			'tipo_cambio':'Tipo de Cambio',
			'numero_comp':'Número de Comprobante',
			'tipo_trans':'Tipo de Transacción',
			'debe_bs':'Debe en Bolivianos',
			'haber_bs':'Haber en Bolivianos',
			'debe_dls':'Debe en Dólares',
			'haber_dls':'Haber en Dólares',
			'dif_bs':'Diferencia Bolivianos',
			'dif_dls':'Diferencia Dólares',
		}
	def __init__(self, *args, **kwargs):
		super(crearEncabezadoForm, self).__init__(*args, **kwargs)
		self.fields['numero_comp'].widget.attrs['readonly'] = True
		
		
class crearEncabezado1Form(forms.ModelForm):
	class Meta:
		model = encabezadoas
		exclude = ['cotizacion', 'comprobante_esc_ant', 'comprobante_esc_antconc', 'comprobante_esc_gen']
		widgets = {
			'fecha':Html5DateInput(format='%Y-%m-%d'),
			'glosa':forms.Textarea(attrs={'class':'form-control'})
			}
		labels = {
			'tipo_cambio':'Tipo de Cambio',
			'numero_comp':'Número de Comprobante',
			'tipo_trans':'Tipo de Transacción',
			'debe_bs':'Debe en Bolivianos',
			'haber_bs':'Haber en Bolivianos',
			'debe_dls':'Debe en Dólares',
			'haber_dls':'Haber en Dólares',
			'dif_bs':'Diferencia Bolivianos',
			'dif_dls':'Diferencia Dólares',
			'entregado':'Entregado a: / Recibido de:'
		}
	def __init__(self, *args, **kwargs):
		comprobante_esc = kwargs.pop("comp", None)
		Cotizacion = kwargs.pop("cot", None)
		super(crearEncabezado1Form, self).__init__(*args, **kwargs)
		if comprobante_esc:
			self.fields['glosa'].initial = comprobante_esc.concepto
			self.fields['fecha'].initial = comprobante_esc.fecha
			self.fields['numero_comp'].initial = comprobante_esc.num_comprobante
			self.fields['tipo_trans'].initial = comprobante_esc.tipo_com
			self.fields['entregado'].initial = comprobante_esc.proovedor.nombre_proov
		else:
			self.fields['glosa'].initial = " "
		if Cotizacion:
			self.fields['tipo_cambio'].initial = Cotizacion.tipo_c
		else:
			self.fields['tipo_cambio'].initial = 0

class crearEncabezado2Form(forms.ModelForm):
	class Meta:
		model = encabezadoas
		exclude = ['cotizacion', 'comprobante_esc_ant', 'comprobante_esc_antconc', 'comprobante_esc_gen']
		widgets = {
			'fecha':Html5DateInput(format='%Y-%m-%d'),
			'glosa':forms.Textarea(attrs={'class':'form-control'})
			}
		labels = {
			'tipo_cambio':'Tipo de Cambio',
			'numero_comp':'Número de Comprobante',
			'tipo_trans':'Tipo de Transacción',
			'debe_bs':'Debe en Bolivianos',
			'haber_bs':'Haber en Bolivianos',
			'debe_dls':'Debe en Dólares',
			'haber_dls':'Haber en Dólares',
			'dif_bs':'Diferencia Bolivianos',
			'dif_dls':'Diferencia Dólares',
			'entregado':'Entregado a: / Recibido de:'
		}
	def __init__(self, *args, **kwargs):
		comprobante_esc = kwargs.pop("comp", None)
		Cotizacion = kwargs.pop("cot", None)
		super(crearEncabezado2Form, self).__init__(*args, **kwargs)
		if comprobante_esc:
			self.fields['glosa'].initial = comprobante_esc.concepto
			self.fields['fecha'].initial = comprobante_esc.fecha
			self.fields['numero_comp'].initial = comprobante_esc.num_comprobante
			self.fields['tipo_trans'].initial = comprobante_esc.tipo_com
			self.fields['entregado'].initial = comprobante_esc.entrega
		else:
			self.fields['glosa'].initial = " "
		if Cotizacion:
			self.fields['tipo_cambio'].initial = Cotizacion.tipo_c
		else:
			self.fields['tipo_cambio'].initial = 0

class crearAsientoForm(forms.ModelForm):
	class Meta:
		model = asiento
		exclude = [" "]
		widgets = {
			'nivel_cinco':autocomplete.ModelSelect2(url='contabilidad:asiento_autocomplete'),
			'auxiliar':forms.HiddenInput(),
			'auxiliar_s':forms.HiddenInput(),
			'estado':forms.HiddenInput()
		}
	def __init__(self, *args, **kwargs):
		super(crearAsientoForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({'class': 'form-control'})
		
            	
		
crearAsientoFormSet = inlineformset_factory(encabezadoas, asiento, form=crearAsientoForm , extra=7, min_num=1, validate_min=True)
updateAsientoFormSet = inlineformset_factory(encabezadoas, asiento, form=crearAsientoForm , extra=1)


class searchForm(forms.Form):
	search = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Busqueda por...'}))

class searchFormLib(forms.Form):
	search = forms.CharField(label="Desde", help_text="Fecha Inicio", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control','placeholder':'Fecha Inicio'}))
	search1 = forms.CharField(label="Hasta", help_text="Fecha Fin", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control','placeholder':'Fecha Fin'}))
	search2 = forms.CharField(label="Codigo", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Código de la Cuenta'}))

class crearPlanCuenta1Form(forms.ModelForm):
	class Meta:
		model = nivel_uno
		exclude = ['']
		labels = {
			'descripcion':'Nombre de la Cuenta'
		}

class crearPlanCuenta2Form(forms.ModelForm):
	class Meta:
		model = nivel_dos
		exclude = ['']
		labels = {
			'codigo':'Código de la Cuenta',
			'descripcion':'Nombre de la Cuenta',
			'nivel_uno':'Grupo'
		}
		widgets = {
			'nivel_uno':autocomplete.ModelSelect2(url='contabilidad:nivel_uno_autocomplete'),
			'codigo':forms.HiddenInput(),
		}

	def __init__(self, *args, **kwargs):
		nivel = kwargs.pop("niv", None)
		super(crearPlanCuenta2Form, self).__init__(*args, **kwargs)
		if nivel:
			self.fields['codigo'].initial = nivel.codigo
		else:
			self.fields['codigo'].initial = 0

class crearPlanCuenta3Form(forms.ModelForm):
	class Meta:
		model = nivel_tres
		exclude = ['']
		labels = {
			'codigo':'Código de la Cuenta',
			'descripcion':'Nombre de la Cuenta',
			'nivel_uno':'Grupo',
			'nivel_dos':'Rubro'
		}
		widgets = {
			'nivel_uno':autocomplete.ModelSelect2(url='contabilidad:nivel_uno_autocomplete'),
			'nivel_dos':autocomplete.ModelSelect2(url='contabilidad:nivel_dos_autocomplete', forward=['nivel_uno']),
			'codigo':forms.HiddenInput(),
		}

	def __init__(self, *args, **kwargs):
		nivel = kwargs.pop("niv", None)
		super(crearPlanCuenta3Form, self).__init__(*args, **kwargs)
		if nivel:
			self.fields['codigo'].initial = nivel.codigo
		else:
			self.fields['codigo'].initial = '0'

class crearPlanCuenta4Form(forms.ModelForm):
	class Meta:
		model = nivel_cuatro
		exclude = ['']
		labels = {
			'descripcion':'Nombre de la Cuenta',
			'nivel_uno':'Grupo',
			'nivel_dos':'Rubro',
			'nivel_tres':'Título'
		}
		widgets = {
			'nivel_uno':autocomplete.ModelSelect2(url='contabilidad:nivel_uno_autocomplete'),
			'nivel_dos':autocomplete.ModelSelect2(url='contabilidad:nivel_dos_autocomplete', forward=['nivel_uno']),
			'nivel_tres':autocomplete.ModelSelect2(url='contabilidad:nivel_tres_autocomplete', forward=['nivel_dos']),
			'codigo':forms.HiddenInput()
		}

class updatePlanCuenta4Form(forms.ModelForm):
	class Meta:
		model = nivel_cuatro
		exclude = ['']
		labels = {
			'codigo':'Código de la Cuenta',
			'descripcion':'Nombre de la Cuenta',
			'nivel_uno':'Grupo',
			'nivel_dos':'Rubro',
			'nivel_tres':'Título'
		}
		widgets = {
			'nivel_uno':autocomplete.ModelSelect2(url='contabilidad:nivel_uno_autocomplete'),
			'nivel_dos':autocomplete.ModelSelect2(url='contabilidad:nivel_dos_autocomplete', forward=['nivel_uno']),
			'nivel_tres':autocomplete.ModelSelect2(url='contabilidad:nivel_tres_autocomplete', forward=['nivel_dos']),
		}

class crearPlanCuenta5Form(forms.ModelForm):
	class Meta:
		model = nivel_cinco
		exclude = ['']
		labels = {
			'descripcion':'Nombre de la Cuenta',
			'nivel_uno':'Grupo',
			'nivel_dos':'Rubro',
			'nivel_tres':'Título',
			'nivel_cuatro':'Cuenta'
		}
		widgets = {
			'nivel_uno':autocomplete.ModelSelect2(url='contabilidad:nivel_uno_autocomplete'),
			'nivel_dos':autocomplete.ModelSelect2(url='contabilidad:nivel_dos_autocomplete', forward=['nivel_uno']),
			'nivel_tres':autocomplete.ModelSelect2(url='contabilidad:nivel_tres_autocomplete', forward=['nivel_dos']),
			'nivel_cuatro':autocomplete.ModelSelect2(url='contabilidad:nivel_cuatro_autocomplete', forward=['nivel_tres']),
			'codigo':forms.HiddenInput()
		}

class updatePlanCuenta5Form(forms.ModelForm):
	class Meta:
		model = nivel_cinco
		exclude = ['']
		labels = {
			'codigo':'Código de la Cuenta',
			'descripcion':'Nombre de la Cuenta',
			'nivel_uno':'Grupo',
			'nivel_dos':'Rubro',
			'nivel_tres':'Título',
			'nivel_cuatro':'Cuenta'
		}
		widgets = {
			'nivel_uno':autocomplete.ModelSelect2(url='contabilidad:nivel_uno_autocomplete'),
			'nivel_dos':autocomplete.ModelSelect2(url='contabilidad:nivel_dos_autocomplete', forward=['nivel_uno']),
			'nivel_tres':autocomplete.ModelSelect2(url='contabilidad:nivel_tres_autocomplete', forward=['nivel_dos']),
			'nivel_cuatro':autocomplete.ModelSelect2(url='contabilidad:nivel_cuatro_autocomplete', forward=['nivel_tres']),
		}

class crearFacturaForm(forms.ModelForm):
	CHOICES = (('1','Sin derecho a crédito fiscal'),('2','Gasolina'),('3','Ninguno'))
	retencion = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	class Meta:
		model = Factura
		exclude = ['asiento']
		widgets = {
			'fecha_fac':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'estado':forms.HiddenInput(),
			'tipo_fac':forms.Select(attrs={'class':'form-control'}),
			'sucursal':forms.TextInput(attrs={'class':'form-control'}),
			'nit_prov':forms.TextInput(attrs={'class':'form-control'}),
			'nro_dui':forms.TextInput(attrs={'class':'form-control'}),
			'nro_aut':forms.TextInput(attrs={'class':'form-control'}),
			'nro_fact':forms.TextInput(attrs={'class':'form-control'}),
			'cod_cont':forms.TextInput(attrs={'class':'form-control'}),
			'nomb_razon':forms.TextInput(attrs={'class':'form-control'}),
			'importe_fac':forms.TextInput(attrs={'class':'form-control'}),
			'importe_credit':forms.TextInput(attrs={'class':'form-control'}),
			'subtot':forms.TextInput(attrs={'class':'form-control'}),
			'descuento':forms.TextInput(attrs={'class':'form-control'}),
			'base_credito':forms.TextInput(attrs={'class':'form-control'}),
			'credit_fisc':forms.TextInput(attrs={'class':'form-control'}),
			}
		labels = {
			'tipo_fac':'Tipo de Factura',
			'fecha_fac':'Fecha de la Factura o DUI',
			'nit_prov':'NIT del Proveedor',
			'nro_dui':'Número DUI',
			'nro_aut':'Número de Autorización',
			'nro_fact':'Número de Factura',
			'cod_cont':'Código de Control',
			'nomb_razon':'Nombre o razón social',
			'importe_fac':'Importe total de la compra',
			'importe_credit':'Importe no sujeto a crédito fiscal',
			'subtot':'Subtotal',
			'descuento':'Descuentos, bonificaciones y rebajas obtenidas',
			'base_credito':'Importe base para crédito fiscal',
			'credit_fisc':'Crédito Fiscal(IVA 13%)',
		}
	def __init__(self, *args, **kwargs):
		asiento = kwargs.pop("asi", None)
		super(crearFacturaForm, self).__init__(*args, **kwargs)
		if asiento:
			self.fields['importe_fac'].initial = asiento.auxiliar_s
		else:
			self.fields['importe_fac'].initial = 0

class crearFacturaVForm(forms.ModelForm):
	class Meta:
		model = Factura_V
		exclude = ['asiento']
		widgets = {
			'fecha_fac':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'estado':forms.HiddenInput(),
			'tipo_fac':forms.Select(attrs={'class':'form-control'}),
			'sucursal':forms.TextInput(attrs={'class':'form-control'}),
			'nit_prov':forms.TextInput(attrs={'class':'form-control'}),
			'nro_dui':forms.TextInput(attrs={'class':'form-control'}),
			'nro_aut':forms.TextInput(attrs={'class':'form-control'}),
			'nro_fact':forms.TextInput(attrs={'class':'form-control'}),
			'cod_cont':forms.TextInput(attrs={'class':'form-control'}),
			'nomb_razon':forms.TextInput(attrs={'class':'form-control'}),
			'importe_fac':forms.TextInput(attrs={'class':'form-control'}),
			'importe_credit':forms.TextInput(attrs={'class':'form-control'}),
			'subtot':forms.TextInput(attrs={'class':'form-control'}),
			'descuento':forms.TextInput(attrs={'class':'form-control'}),
			'base_credito':forms.TextInput(attrs={'class':'form-control'}),
			'credit_fisc':forms.TextInput(attrs={'class':'form-control'}),
			}
		labels = {
			'tipo_fac':'Tipo de Factura',
			'fecha_fac':'Fecha de la Factura',
			'nit_prov':'NIT del Proveedor',
			'estado_p':'Estado',
			'nit_cliente':'NIT/CI Cliente',
			'importe_ice':'Importe ICE/IEHD/Tasas',
			'export_oper':'Exportaciones y Operaciones exentas',
			'ventas_grav':'Ventas gravadas a tasa cero',
			'nro_aut':'Número de Autorización',
			'nro_fact':'Número de Factura',
			'cod_cont':'Código de Control',
			'nomb_razon':'Nombre o razón social',
			'importe_fac':'Importe total de la compra',
			'importe_credit':'Importe no sujeto a crédito fiscal',
			'subtot':'Subtotal',
			'descuento':'Descuentos, bonificaciones y rebajas obtenidas',
			'base_debito':'Importe base para débito fiscal',
			'debito_fisc':'Débito Fiscal(IVA 13%)',
		}
	def __init__(self, *args, **kwargs):
		asiento = kwargs.pop("asi", None)
		super(crearFacturaVForm, self).__init__(*args, **kwargs)
		self.fields['sucursal'].widget.attrs['readonly'] = True
		self.fields['subtot'].widget.attrs['readonly'] = True
		self.fields['base_debito'].widget.attrs['readonly'] = True
		self.fields['debito_fisc'].widget.attrs['readonly'] = True
		if asiento:
			self.fields['importe_fac'].initial = asiento.auxiliar_s
		else:
			self.fields['importe_fac'].initial = 0

class crearFacturaBolForm(forms.ModelForm):
	class Meta:
		model = Factura
		exclude = ['asiento']
		widgets = {
			'fecha_fac':Html5DateInput(format='%Y-%m-%d'),
			'estado':forms.HiddenInput(),
			}
		labels = {
			'tipo_fac':'Tipo de Factura',
			'fecha_fac':'Fecha de Emisión',
			'nit_prov':'NIT Línea Aérea',
			'nro_dui':'Número DUI',
			'nro_aut':'Número de Autorización',
			'nro_fact':'Número de Boleto - Ticket Electrónico',
			'cod_cont':'Código de Control',
			'nomb_razon':'Razón Social Línea Aérea',
			'importe_fac':'Importe Boleto',
			'importe_credit':'Importe no sujeto a crédito fiscal',
			'subtot':'Subtotal',
			'descuento':'Descuentos, bonificaciones y rebajas obtenidas',
			'base_credito':'Importe base para crédito fiscal',
			'credit_fisc':'Crédito Fiscal(IVA 13%)',
		}
	def __init__(self, *args, **kwargs):
		asiento = kwargs.pop("asi", None)
		super(crearFacturaBolForm, self).__init__(*args, **kwargs)
		self.fields['nro_aut'].initial = '1'
		if asiento:
			self.fields['importe_fac'].initial = asiento.auxiliar_s
		else:
			self.fields['importe_fac'].initial = 0

class crearFacturaImpForm(forms.ModelForm):
	cod_aduana = forms.CharField(max_length=3, label='Código de la Aduana')
	tipo_tram = forms.CharField(max_length=1, label='Tipo de Trámite')
	nro_tramite = forms.CharField(max_length=10, label='Número de Trámite')
	class Meta:
		model = Factura
		exclude = ['asiento']
		widgets = {
			'fecha_fac':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'tipo_fac':forms.Select(attrs={'class':'form-control'}),
			'estado':forms.HiddenInput(),
			'sucursal':forms.TextInput(attrs={'class':'form-control'}),
			'nit_prov':forms.TextInput(attrs={'class':'form-control'}),
			'nro_dui':forms.TextInput(attrs={'class':'form-control'}),
			'nro_aut':forms.TextInput(attrs={'class':'form-control'}),
			'nro_fact':forms.TextInput(attrs={'class':'form-control'}),
			'cod_cont':forms.TextInput(attrs={'class':'form-control'}),
			'nomb_razon':forms.TextInput(attrs={'class':'form-control'}),
			'importe_fac':forms.TextInput(attrs={'class':'form-control'}),
			'importe_credit':forms.TextInput(attrs={'class':'form-control'}),
			'subtot':forms.TextInput(attrs={'class':'form-control'}),
			'descuento':forms.TextInput(attrs={'class':'form-control'}),
			'base_credito':forms.TextInput(attrs={'class':'form-control'}),
			'credit_fisc':forms.TextInput(attrs={'class':'form-control'}),
			'cod_aduana':forms.TextInput(attrs={'class':'form-control'}),
			'tipo_tram':forms.TextInput(attrs={'class':'form-control'}),
			'nro_tramite':forms.TextInput(attrs={'class':'form-control'}),
			}
		labels = {
			'tipo_fac':'Tipo de Factura',
			'fecha_fac':'Fecha de la Factura o DUI',
			'nit_prov':'NIT del Proveedor',
			'nro_dui':'Número DUI',
			'nro_aut':'Número de Autorización',
			'nro_fact':'Número de Factura',
			'cod_cont':'Código de Control',
			'nomb_razon':'Nombre o razón social',
			'importe_fac':'Importe total de la compra',
			'importe_credit':'Importe no sujeto a crédito fiscal',
			'subtot':'Subtotal',
			'descuento':'Descuentos, bonificaciones y rebajas obtenidas',
			'base_credito':'Importe base para crédito fiscal',
			'credit_fisc':'Crédito Fiscal(IVA 13%)',
			'cod_aduana':'Código de la Aduana',
			'tipo_tram':'Tipo de Trámite',
			'nro_tramite':'Número de Trámite'
		}
	def __init__(self, *args, **kwargs):
		asiento = kwargs.pop("asi", None)
		super(crearFacturaImpForm, self).__init__(*args, **kwargs)
		self.fields['tipo_tram'].initial = 'C'
		self.fields['nro_aut'].initial = '3'
		if asiento:
			self.fields['importe_fac'].initial = asiento.auxiliar_s
		else:
			self.fields['importe_fac'].initial = 0

class crearCotizacionForm(forms.ModelForm):
	class Meta:
		model = Cotizacion
		exclude = [" "]
		widgets = {
		'fecha':Html5DateInput(format='%Y-%m-%d'),
		}
		labels = {
			'tipo_c':'Tipo de cambio',
			'ufv':'UFV'
		}

class crearProyectoForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		exclude = [" "]
		labels = {
			'nombre':'Nombre del Proyecto',
			'codigo':'Código del Proyecto'
		}

class crearBancarizacionForm(forms.ModelForm):
	class Meta:
		model = bancarizacion
		exclude = ["factura"]
		widgets = {
			'fecha':Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}),
			'estado':forms.HiddenInput()
		}
		labels = {
			'modalidad':'Modalidad de Transacción',
			'numero_contr':'Número de Contrato',
			'num_cuenta_doc':'Número de Cuenta del Documento de Pago',
			'importe':'Importe Pagado',
			'monto_acum':'Monto Acumulado de Pagos Parciales Otorgados',
			'nit_entidad':'NIT de la Entidad Financiera Emisora del Documento de Pago',
			'num_trans':'Número de Transacción u Operación de Pago',
			'tipo_docum':'Tipo de Documento de Pago'
		}
	def __init__(self, *args, **kwargs):
		factura = kwargs.pop("fac", None)
		super(crearBancarizacionForm, self).__init__(*args, **kwargs)
		if factura:
			self.fields['importe'].initial = factura.importe_fac
		else:
			self.fields['importe'].initial = 0

class crearGestion(forms.ModelForm):
	class Meta:
		model = gestion
		exclude = ['cerrado']
		labels = {
			'year': 'Gestion',
		}

class crearCierreGestionForm(forms.ModelForm):
	class Meta:
		model = gestion
		fields = ['cerrado']
		labels = {
			'cerrado': 'Cerrar Gestion'
		}

class renumerarComprobantesForm(forms.Form):
	campo = forms.BooleanField(label="Renumerar")

class repCostoServicioForm(forms.Form):
	campo = forms.CharField(label="Desde", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))
	campo1 = forms.CharField(label="Hasta", help_text="", widget=Html5DateInput(format='%Y-%m-%d', attrs={'class':'form-control'}))

class XlsInputForm(forms.Form):
	input_excel = forms.FileField(required=True, label=' ', help_text='Seleccione un archivo en formato .xls ó .xlsx', widget=forms.FileInput(attrs={'class':'form-control', 'accept':'.xls,.xlsx'}))

	def clean_input_excel(self):
		IMPORT_FILE_TYPES = ['.xlsx','.xls']
		input_excel = self.cleaned_data['input_excel']
		extension = os.path.splitext(input_excel.name)[1]
		if not (extension in IMPORT_FILE_TYPES):
			raise forms.ValidationError(u'no es un tipo valido')
		else:
			return input_excel