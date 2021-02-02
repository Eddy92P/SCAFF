# -*- coding: utf-8 -*-
from django.shortcuts import render
from almacenes.forms import *
from almacenes.models import *
from activos_f.models import *
from usuarios.models import *
from contabilidad.views import *
# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404

from easy_pdf.views import PDFTemplateView
from django.db.models import Q

import datetime
from itertools import chain
from operator import attrgetter
from django.db.models import F
from django.db.models import Sum
from django.db.models import Count, Avg
from django.db.models import Subquery, OuterRef

from itertools import chain
from operator import attrgetter, methodcaller

from openpyxl import Workbook
from decimal import Decimal
"""
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.http import HttpResponse

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus import Table,TableStyle
from reportlab.lib import colors
"""

class crearProveedor(CreateView):
	form_class = crearProveedorForm
	template_name = 'almacen/nuevoproveedor.html'
	success_url = reverse_lazy('almacenes:listaproveedor')

class updateProveedor(UpdateView):
	model = proveedor
	form_class = crearProveedorForm
	template_name = 'almacen/nuevoproveedor.html'
	success_url = reverse_lazy('almacenes:listaproveedor')

class listaProveedor(ListView):
	model = proveedor
	template_name = 'almacen/listaproveedor.html'

class crearCliente(CreateView):
	form_class = crearClienteForm
	template_name = 'almacen/nuevocliente.html'
	success_url = reverse_lazy('almacenes:listacliente')

class updateCliente(UpdateView):
	model = cliente
	form_class = crearClienteForm
	template_name = 'almacen/nuevocliente.html'
	success_url = reverse_lazy('almacenes:listacliente')

class listaCliente(CreateView,ListView):
	model = cliente
	form_class = searchForm
	template_name = 'almacen/listacliente.html'
	def get_context_data(self, **kwargs):
		context = super (listaCliente, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearTipoEntrada(CreateView):
	form_class = crearTipoEntradaForm
	template_name = 'almacen/nuevotipo_entrada.html'
	success_url = reverse_lazy('almacenes:listatipo_entrada')

class updateTipoEntrada(UpdateView):
	model = tipo_entrada
	form_class = crearTipoEntradaForm
	template_name = 'almacen/nuevotipo_entrada.html'
	success_url = reverse_lazy('almacenes:listatipo_entrada')

class listaTipoEntrada(CreateView,ListView):
	model = tipo_entrada
	form_class = searchForm
	template_name = 'almacen/listatipo_entrada.html'
	def get_context_data(self, **kwargs):
		context = super (listaTipoEntrada, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearTipoSalida(CreateView):
	form_class = crearTipoSalidaForm
	template_name = 'almacen/nuevotipo_salida.html'
	success_url = reverse_lazy('almacenes:listatipo_salida')

class updateTipoSalida(UpdateView):
	model = tipo_salida
	form_class = crearTipoSalidaForm
	template_name = 'almacen/nuevotipo_salida.html'
	success_url = reverse_lazy('almacenes:listatipo_salida')

class listaTipoSalida(CreateView,ListView):
	model = tipo_salida
	form_class = searchForm
	template_name = 'almacen/listatipo_salida.html'
	def get_context_data(self, **kwargs):
		context = super (listaTipoSalida, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearUnidad(CreateView):
	form_class = crearUnidadForm
	template_name = 'almacen/nuevaunidad.html'
	success_url = reverse_lazy('almacenes:listaunidad')

class updateUnidad(UpdateView):
	model = unidad
	form_class = crearUnidadForm
	template_name = 'almacen/nuevaunidad.html'
	success_url = reverse_lazy('almacenes:listaunidad')

class listaUnidad(CreateView,ListView):
	model = unidad
	form_class = searchForm
	template_name = 'almacen/listaunidad.html'
	def get_context_data(self, **kwargs):
		context = super (listaUnidad, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

#Autocompletado encadenado
"""class almacenAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return almacen.objects.none()
		qs = almacen.objects.all().order_by('id')
		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs"""

class categoriaAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return categoria.objects.none()
		qs = categoria.objects.all().order_by('id')
		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

class subcategoriaAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return subcategoria.objects.none()
		qs = subcategoria.objects.all().order_by('id')
		categoria = self.forwarded.get('categoria', None)
		if categoria:
			qs = qs.filter(categoria=categoria)
		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

class itemAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return item.objects.none()
		qs = item.objects.all().order_by('codigo')
		if self.q:
			qs = qs.filter(Q(nombre__istartswith=self.q) | Q(codigo__icontains=self.q))
		return qs

class itemActAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return item.objects.none()
		qs = item.objects.filter(activo_f=True).order_by('codigo')
		if self.q:
			qs = qs.filter(Q(nombre__istartswith=self.q) | Q(codigo__icontains=self.q))
		return qs

class personalAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return personal.objects.none()
		qs = personal.objects.all().order_by('id')
		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

class proveedorAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return proveedor.objects.none()
		qs = proveedor.objects.all().order_by('id')
		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

class clienteAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return cliente.objects.none()
		qs = cliente.objects.all().order_by('id')
		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

class ubicacionAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return Ubicacion_gen.objects.none()
		qs = Ubicacion_gen.objects.all().order_by('id')
		if self.q:
			qs = qs.filter(ubicacion_g__istartswith=self.q)
		return qs

"""class crearAlmacen(CreateView):
	form_class = crearAlmacenForm
	template_name = 'almacen/crearalmacen.html'
	success_url = reverse_lazy('almacenes:listaalmacenes')

class updateAlmacen(UpdateView):
	model = almacen
	form_class = crearAlmacenForm
	template_name = 'almacen/crearalmacen.html'
	success_url = reverse_lazy('almacenes:listaalmacenes')

class listaAlmacenes(CreateView,ListView):
	model = almacen
	form_class = searchForm
	template_name = 'almacen/listaalmacenes.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaAlmacenes, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list"""

class crearCategoria(CreateView):
	form_class = crearCategoriaForm
	template_name = 'almacen/nuevacategoria.html'
	success_url = reverse_lazy('almacenes:listacategoria')

class updateCategoria(UpdateView):
	model = categoria
	form_class = crearCategoriaForm
	template_name = 'almacen/nuevacategoria.html'
	success_url = reverse_lazy('almacenes:listacategoria')

class listaCategoria(CreateView,ListView):
	model = categoria
	form_class = searchForm
	template_name = 'almacen/listacategoria.html'
	def get_context_data(self, **kwargs):
		context = super (listaCategoria, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearSubCategoria(CreateView):
	form_class = crearSubCategoriaForm
	template_name = 'almacen/nuevasubcategoria.html'
	success_url = reverse_lazy('almacenes:listasubcategoria')

class updateSubCategoria(UpdateView):
	model = subcategoria
	form_class = crearSubCategoriaForm
	template_name = 'almacen/nuevasubcategoria.html'
	success_url = reverse_lazy('almacenes:listasubcategoria')

class listaSubCategoria(CreateView,ListView):
	model = subcategoria
	form_class = searchForm
	template_name = 'almacen/listasubcategoria.html'
	def get_context_data(self, **kwargs):
		context = super (listaSubCategoria, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearItem(CreateView):
	model = item
	form_class = crearItemForm
	template_name = 'almacen/nuevoitem.html'
	success_url = 'almacenes:listaitem'

	def get_context_data(self, **kwargs):
		context = super(crearItem, self).get_context_data(**kwargs)
		return context
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			aux = str(form.subcategoria.categoria.id) + '-' + str(form.subcategoria.id) + '-' + form.codigo.zfill(4)
			form.codigo = aux
			form.save()
			return HttpResponseRedirect(reverse_lazy(self.success_url))
		else:
			return self.render_to_response(self.get_context_data(form=form))

class updateItem(UpdateView):
	model = item
	form_class = crearItemForm
	template_name = 'almacen/nuevoitem.html'
	success_url = reverse_lazy('almacenes:listaitem')

class listaItem(CreateView,ListView):
	model = item
	form_class = searchForm
	template_name = 'almacen/listaitem.html'
	def get_context_data(self, **kwargs):
		context = super (listaItem, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearItemAct(CreateView):
	model = item_act
	form_class = crearItemActForm
	template_name = 'almacen/nuevoitemact.html'
	success_url = 'almacenes:listaitemact'

	def get_context_data(self, **kwargs):
		context = super(crearItemAct, self).get_context_data(**kwargs)
		return context
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return HttpResponseRedirect(reverse_lazy(self.success_url))
		else:
			return self.render_to_response(self.get_context_data(form=form))

class updateItemAct(UpdateView):
	model = item_act
	form_class = crearItemActForm
	template_name = 'almacen/nuevoitemact.html'
	success_url = reverse_lazy('almacenes:listaitemact')

class listaItemAct(ListView):
	model = item_act
	template_name = 'almacen/listaitemact.html'

class listaAltaAct(ListView):
	model = salidaitem
	template_name = 'almacen/listasalidaitemact.html'

	def get_context_data(self, **kwargs):
		context = super (listaAltaAct, self).get_context_data(**kwargs)	
		return context

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list))

	def get_queryset(self):
		object_list = self.model.objects.filter(item__activo_f=True).order_by('id')
		return object_list

class listaSalidaItemf(ListView):
	model = salidaitem
	template_name = 'almacen/listasalidaitemf.html'

# lazys complejos

class ingresoItem(CreateView):
	model_pk = item
	form_class = crearEncabezadoIngresoForm
	template_name = 'almacen/ingresoitem.html'
	success_url = 'almacenes:listaingreso'

	def get_context_data(self, **kwargs):
		context = super(ingresoItem, self).get_context_data(**kwargs)
		return context

	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		crear_ingreso_form_set = crearIngresoItemFormSet()
		crear_personal_form_set = crearPersonalFormSet()
		return self.render_to_response(self.get_context_data(form=form, crear_ingreso_form_set=crear_ingreso_form_set, crear_personal_form_set=crear_personal_form_set))

	def post(self, request, *args, **kwargs):
		self.object = None	
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		crear_ingreso_form_set = crearIngresoItemFormSet(request.POST)
		crear_personal_form_set = crearPersonalFormSet(request.POST)
		if form.is_valid() and crear_ingreso_form_set.is_valid() and crear_personal_form_set.is_valid():
			form1 = form.save(commit=False) 
			crear_personal_form_set.instance = form1
			persona = crear_personal_form_set.save(commit=False)
			crear_ingreso_form_set.instance = form1
			ingreso = crear_ingreso_form_set.save(commit=False)
			for formset in ingreso:
				formset.costo_unit_actualizado = formset.costo_unit
				formset.sub_total_actualizado = formset.sub_total
				a=itemalmacen.objects.get_or_create(item = formset.item)
				if a[0].cantidad >= formset.item.maximo:
					return self.render_to_response(self.get_context_data(form = form, crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set, error='El almacen se encuentra lleno, realice salidas del item ' + a[0].item.nombre))
				elif formset.cantidad >= formset.item.maximo:
					return self.render_to_response(self.get_context_data(form = form, crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el maximo permitido de '+ str(formset.item.maximo) + ' del item ' + a[0].item.nombre + ', por favor verifique los datos'))
				else:
					a[0].cantidad = a[0].cantidad + formset.cantidad
					if a[0].cantidad >= formset.item.maximo:
						return self.render_to_response(self.get_context_data(form = form, crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el maximo permitido de '+ str(formset.item.maximo) + ' del item ' + a[0].item.nombre + ', por favor verifique los datos'))
					else:
						a[0].precio = 0
						a[0].save()
					form1.save()
					crear_personal_form_set.save()
					crear_ingreso_form_set.save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url))
		else:
			return self.render_to_response(self.get_context_data(form=form,  crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set))

class listaIngresoItem(ListView):
	model = encingresoitem
	form_class = searchForm
	template_name = 'almacen/listaingresoitem.html'

	def get_context_data(self, **kwargs):
		context = super (listaIngresoItem, self).get_context_data(**kwargs)
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
		return context

class updateIngresoItem(UpdateView):
	model = encingresoitem
	form_class = crearEncabezadoIngresoForm
	template_name = 'almacen/ingresoitem.html'
	success_url = 'almacenes:listaingreso'

	def get_context_data(self, **kwargs):
		context = super(updateIngresoItem, self).get_context_data(**kwargs)
		pk1 = self.kwargs['pk']
		if 'form' and 'car' in context:
			context['form'] = self.form_class()
			context['car'] = encingresoitem.objects.get(id=pk1)
		return context

	def get_success_url(self):
		return reverse_lazy(self.success_url, kwargs = {'pk': self.get_object().encingresoitem.pk})

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		crear_ingreso_form_set = updateIngresoItemFormSet(instance=self.object)
		crear_personal_form_set = updatePersonalFormSet(instance=self.object)
		return self.render_to_response(self.get_context_data(form=form, crear_ingreso_form_set=crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set))

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		pk1=self.kwargs['pk']
		form = self.form_class(request.POST, instance=self.model.objects.get(id=pk1))
		crear_ingreso_form_set = updateIngresoItemFormSet(request.POST, instance=self.model.objects.get(id=pk1))
		crear_personal_form_set = updatePersonalFormSet(request.POST, instance=self.model.objects.get(id=pk1))
		if form.is_valid() and crear_ingreso_form_set.is_valid() and crear_personal_form_set.is_valid():
			aux = 0
			form1 = form.save(commit=False) 
			crear_personal_form_set.instance = form1
			persona = crear_personal_form_set.save(commit=False)
			crear_ingreso_form_set.instance = form1
			ingreso = crear_ingreso_form_set.save(commit=False)
			for formset in ingreso:
				a = itemalmacen.objects.get_or_create(item = formset.item)
				i = ingresoitem.objects.filter(item = formset.item, encingresoitem=pk1, id=formset.id).aggregate(total=Sum('cantidad'))
				if a[0].cantidad >= formset.item.maximo:
					return self.render_to_response(self.get_context_data(form = form, crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set, error='El almacen se encuentra lleno, realice salidas del item ' + a.item.nombre))
				elif formset.cantidad >= formset.item.maximo:
					return self.render_to_response(self.get_context_data(form = form, crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el maximo permitido de '+ str(formset.item.maximo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
				else:
					if i['total'] == None:
						a[0].cantidad = a[0].cantidad + formset.cantidad
						if a[0].cantidad >= formset.item.maximo:
							return self.render_to_response(self.get_context_data(form = form, crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el maximo permitido de '+ str(formset.item.maximo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
						else:
							a[0].save()
					elif((formset.cantidad > i['total'])):
						aux = formset.cantidad - i['total']
						a[0].cantidad = a[0].cantidad + aux
						if a[0].cantidad >= formset.item.maximo:
							return self.render_to_response(self.get_context_data(form = form, crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el maximo permitido de '+ str(formset.item.maximo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
						else:
							a[0].save()
					elif(formset.cantidad < i['total']):
						aux = i['total'] - formset.cantidad
						a[0].cantidad = a[0].cantidad + aux
						if a[0].cantidad >= formset.item.maximo:
							return self.render_to_response(self.get_context_data(form = form, crear_ingreso_form_set = crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el maximo permitido de '+ str(formset.item.maximo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
						else:
							a[0].save()	
					form1.save()
					crear_personal_form_set.save()
					crear_ingreso_form_set.save()
			return HttpResponseRedirect(reverse_lazy(self.success_url))
		else:
			return self.render_to_response(self.get_context_data(form=form, crear_ingreso_form_set=crear_ingreso_form_set, crear_personal_form_set = crear_personal_form_set))

class salidaItem(CreateView):
	model_pk = item
	form_class = crearEncabezadoSalidaForm
	second_form_class = crearSalidaItemForm
	template_name = 'almacen/salidaitem.html'
	success_url = 'almacenes:listasalida'

	def get_context_data(self, **kwargs):
		context = super (salidaItem, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		return context

	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		crear_personal_form_set = crearPersonalSFormSet()
		crear_salida_form_set = crearSalidaItemFormSet()
		return self.render_to_response(self.get_context_data(form=form, crear_salida_form_set=crear_salida_form_set, crear_personal_form_set=crear_personal_form_set))
	
	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		crear_personal_form_set = crearPersonalSFormSet(request.POST)
		crear_salida_form_set = crearSalidaItemFormSet(request.POST)
		if form.is_valid() and crear_salida_form_set.is_valid() and crear_personal_form_set.is_valid():
			from django.db.models import Avg
			form1 = form.save(commit=False)
			crear_salida_form_set.instance = form1
			crear_personal_form_set.instance = form1
			persona = crear_personal_form_set.save(commit=False)
			salida = crear_salida_form_set.save(commit=False)
			for formset in salida:
				a = itemalmacen.objects.get(item = formset.item)
				if a.cantidad < formset.cantidad:
					return self.render_to_response(self.get_context_data(form1 = form1, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el stock actual de '+ str(a.cantidad) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
				elif a.cantidad < formset.item.minimo:
					return self.render_to_response(self.get_context_data(form = form, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el minimo permitido de '+ str(formset.item.minimo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
				else:
					try:
						aux = ingresoitem.objects.filter(item = formset.item, encingresoitem__fecha__lte=form1.fecha).aggregate(total=Sum('cantidad'))
						aux1 = salidaitem.objects.filter(item = formset.item, encsalidaitem__fecha__lte=form1.fecha).aggregate(total=Sum('cantidad'))
						aux2 = ingresoitem.objects.filter(item = formset.item, encingresoitem__fecha__lte=form1.fecha).aggregate(total=Sum('sub_total'))
						
						if aux1['total'] == None:
							aux1['total'] = 0
						res = aux['total'] - aux1['total']
						res1 = aux2['total']/Decimal(res)
						formset.costo_unit = round(res1, 2)
						formset.sub_total = Decimal(formset.cantidad) * res1
						a.cantidad = a.cantidad - formset.cantidad
						if a.cantidad < formset.item.minimo:
							return self.render_to_response(self.get_context_data(form = form, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el minimo permitido de '+ str(formset.item.minimo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
						else:
							form1.save()
							crear_salida_form_set.save()
							crear_personal_form_set.save()
							form.save_m2m()
							a.save()
					except Exception as e:
						raise ValueError('La cantidad de salida excede el saldo existente a la fecha especificada, o la fecha de salida es anterior a la fecha de ingreso, verifique los datos')

			return  HttpResponseRedirect(reverse_lazy(self.success_url))
		else:
			return self.render_to_response(self.get_context_data(form=form, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set))

class listaSalidaItem(CreateView,ListView):
	model = encsalidaitem
	form_class = searchForm
	template_name = 'almacen/listasalidaitem.html'

	def get_context_data(self, **kwargs):
		context = super (listaSalidaItem, self).get_context_data(**kwargs)
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
				#kwargs['id']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.all().order_by('id')
		return object_list

class updateSalidaItem(UpdateView):
	model = encsalidaitem
	form_class = crearEncabezadoSalidaForm
	template_name = 'almacen/salidaitem.html'
	success_url = 'almacenes:listasalida'

	def get_context_data(self, **kwargs):
		context = super(updateSalidaItem, self).get_context_data(**kwargs)
		pk1 = self.kwargs['pk']
		if 'form' and 'car' in context:
			context['form'] = self.form_class()
			context['car'] = encsalidaitem.objects.get(id=pk1)
		return context

	def get_success_url(self):
		return reverse_lazy(self.success_url, kwargs = {'pk': self.get_object().encsalidaitem.pk})

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		crear_salida_form_set = crearSalidaItemFormSet(instance=self.object)
		crear_personal_form_set = updatePersonalSFormSet(instance=self.object)
		return self.render_to_response(self.get_context_data(form=form, crear_salida_form_set=crear_salida_form_set, crear_personal_form_set=crear_personal_form_set))

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		pk1=self.kwargs['pk']
		form = self.form_class(request.POST, instance=self.model.objects.get(id=pk1))
		crear_salida_form_set = crearSalidaItemFormSet(request.POST, instance=self.model.objects.get(id=pk1))
		crear_personal_form_set = updatePersonalSFormSet(request.POST, instance=self.model.objects.get(id=pk1))
		if form.is_valid() and crear_salida_form_set.is_valid():
			form1 = form.save(commit=False)
			crear_salida_form_set.instance = form1
			persona = crear_personal_form_set.save(commit=False)
			salida = crear_salida_form_set.save(commit=False)
			for formset in salida:
				a = itemalmacen.objects.get(item = formset.item)
				if a.cantidad < formset.cantidad:
					return self.render_to_response(self.get_context_data(form = form, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el stock actual de '+ str(a.cantidad) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
				elif a.cantidad < formset.item.minimo:
					return self.render_to_response(self.get_context_data(form = form, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el minimo permitido de '+ str(formset.item.minimo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
				else:
					try:
						aux = ingresoitem.objects.filter(item = formset.item, encingresoitem__fecha__lte=form1.fecha).aggregate(total=Sum('cantidad'))
						aux1 = salidaitem.objects.filter(item = formset.item, encsalidaitem__fecha__lte=form1.fecha).aggregate(total=Sum('cantidad'))
						aux2 = ingresoitem.objects.filter(item = formset.item, encingresoitem__fecha__lte=form1.fecha).aggregate(total=Sum('sub_total'))
						
						if aux1['total'] == None:
							aux1['total'] = 0
						res = aux['total'] - aux1['total']
						res1 = aux2['total']/Decimal(res)
						if (formset.costo_unit == 0) | (formset.sub_total == 0):
							formset.costo_unit = round(res1, 2)
							formset.sub_total = Decimal(formset.cantidad) * res1
						s = salidaitem.objects.filter(item = formset.item, encsalidaitem=pk1, id=formset.id).aggregate(total=Sum('cantidad'))
						if s['total'] == None:
							a.cantidad = a.cantidad - formset.cantidad
							if a.cantidad < formset.item.minimo:
								return self.render_to_response(self.get_context_data(form = form, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el mínimo permitido de '+ str(formset.item.minimo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
							else:
								a.save()
						elif(formset.cantidad > s['total']):
							aux = formset.cantidad - s['total']
							a.cantidad = a.cantidad - aux
							if a.cantidad < formset.item.minimo:
								return self.render_to_response(self.get_context_data(form = form, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el mínimo permitido de '+ str(formset.item.minimo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
							else:
								a.save()
						elif(formset.cantidad < s['total']):
							aux = s['total'] - formset.cantidad
							a.cantidad = a.cantidad - aux
							if a.cantidad < formset.item.minimo:
								return self.render_to_response(self.get_context_data(form = form, crear_salida_form_set = crear_salida_form_set, crear_personal_form_set = crear_personal_form_set, error='La cantidad excede el mínimo permitido de '+ str(formset.item.minimo) + ' del item ' + a.item.nombre + ', por favor verifique los datos'))
							else:
								a.save()
						form1.save()
						crear_salida_form_set.save()
						crear_personal_form_set.save()
						form.save_m2m()
					except Exception as e:
						raise ValueError('La cantidad de salida excede el saldo existente a la fecha especificada, o la fecha de salida es anterior a la fecha de ingreso, verifique los datos')
					
			return HttpResponseRedirect(reverse_lazy(self.success_url))
		else:
			return self.render_to_response(self.get_context_data(form=form, crear_salida_form_set=crear_salida_form_set))

class listaItemT(CreateView,ListView):
	model = item
	form_class = searchForm
	template_name = 'almacen/listaitemt.html'
	def get_context_data(self, **kwargs):
		context = super (listaItemT, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				id = form.cleaned_data['search']
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class generarComprobanteIng(PDFTemplateView):
	template_name = "almacen/comprobante_ingresoitem.html"
	def get_context_data(self, **kwargs):
		context = super(generarComprobanteIng, self).get_context_data(**kwargs)
		pk1 = self.kwargs.get('pk')
		try:
			context['res'] = encingresoitem.objects.get(id=pk1)
			context['user'] = self.request.user
		except:
			raise Http404
		return context

class generarComprobanteSal(PDFTemplateView):
	template_name = "almacen/comprobante_salidaitem.html"
	def get_context_data(self, **kwargs):
		context = super(generarComprobanteSal, self).get_context_data(**kwargs)
		pk1 = self.kwargs.get('pk')
		try:
			context['res'] = encsalidaitem.objects.get(id=pk1)
			context['user'] = self.request.user
		except:
			raise Http404
		return context

class reporteDiarioETemplate(FormView):
	form_class = reporteDiarioEForm
	template_name = "almacen/rep_diario_e_temp.html"
	def get_context_data(self, **kwargs):
		context = super(reporteDiarioETemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class reporteDiarioE(PDFTemplateView):
	template_name = "almacen/rep_diario_e.html"
	def get_context_data(self, **kwargs):
		context = super(reporteDiarioE, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		context['res'] = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2)).order_by('encingresoitem__fecha')
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2

		return context

class reporteDiarioSTemplate(FormView):
	form_class = reporteDiarioEForm
	template_name = "almacen/rep_diario_s_temp.html"
	def get_context_data(self, **kwargs):
		context = super(reporteDiarioSTemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class reporteDiarioS(PDFTemplateView):
	template_name = "almacen/rep_diario_s.html"
	def get_context_data(self, **kwargs):
		context = super(reporteDiarioS, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")	
		context['res'] = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2)).order_by('encsalidaitem__fecha')
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2
		return context

class reporteKardexVal(PDFTemplateView):
	template_name = "almacen/kardex_fisico_v.html"
	def get_context_data(self, **kwargs):
		context = super(reporteKardexVal, self).get_context_data(**kwargs)
		op = 0
		op1 = 0
		suma_c_e = 0
		suma_sub_e = 0
		suma_c_s = 0
		suma_sub_s = 0
		saldo = []
		saldo1 = []
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		campo2 = self.request.GET.get('campo2')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		aux1 = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1,f2), item__codigo=campo2)
		aux2 = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1,f2), item__codigo=campo2)
		lista = list(sorted(chain(aux1, aux2), key=methodcaller('encabezado_f')))
		
		for i in lista:
			if i.encabezado().tipo() == "E":
				suma_c_e = suma_c_e + i.cantidad
				suma_sub_e = suma_sub_e + i.sub_total
				op = op + i.cantidad
				op1 = op1 + i.sub_total
				saldo.append(op)
				saldo1.append(op1)
			else:
				suma_c_s = suma_c_s + i.cantidad
				suma_sub_s = suma_sub_s + i.sub_total
				op = op - i.cantidad
				op1 = op1 - i.sub_total
				saldo.append(op)
				saldo1.append(op1)

		lista_res = zip(lista, saldo, saldo1)
		context['cant_e'] = suma_c_e
		context['sub_e'] = suma_sub_e
		context['cant_s'] = suma_c_s
		context['sub_s'] = suma_sub_s
		context['res'] = lista_res
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2
		
		return context

class resumenKardexTemplate(FormView):
	form_class = reporteResKardexForm
	template_name = "almacen/res_kardex.html"
	def get_context_data(self, **kwargs):
		context = super(resumenKardexTemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class resumenKardex(PDFTemplateView):
	template_name = "almacen/resumenKardex.html"
	model_pk = item
	def get_context_data(self, **kwargs):
		context = super(resumenKardex, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		f3 = f1 - datetime.timedelta(days=1)
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		fecha3 = f3.strftime("%d/%m/%Y")
		b = 0
		c = 0

		d = 0
		e = 0

		f = 0

		tot_saldo_a = 0
		tot_saldo_e = 0
		tot_saldo_s = 0
		tot_saldo = 0

		salida = []

		saldo_c = []
		cantidad_e = []
		cantidad_s = []
		saldo_sub = []
		sub_total_e = []
		sub_total_s = []

		saldo_c_a = []
		cantidad_e_a = []
		cantidad_s_a = []
		saldo_sub_a = []
		sub_total_e_a = []
		sub_total_s_a = []

		saldo_c_t = []
		saldo_sub_t = []

		try:
			aux_a = item.objects.filter(ingresoitem__encingresoitem__fecha__lte=f3).distinct().order_by('codigo').annotate(total=Sum('ingresoitem__cantidad'))
			aux1_a = item.objects.filter(salidaitem__encsalidaitem__fecha__lte=f3).distinct().order_by('codigo').annotate(total=Sum('salidaitem__cantidad'))
			aux2_a = item.objects.filter(ingresoitem__encingresoitem__fecha__lte=f3).distinct().order_by('codigo').annotate(total=Sum('ingresoitem__sub_total'))
			aux3_a = item.objects.filter(salidaitem__encsalidaitem__fecha__lte=f3).distinct().order_by('codigo').annotate(total=Sum('salidaitem__sub_total'))
				
			resp = item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).order_by('codigo').distinct()
			resp_a = item.objects.filter(ingresoitem__encingresoitem__fecha__lte=f3).order_by('codigo').distinct()
	
			aux = item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).distinct().order_by('codigo').annotate(total=Sum('ingresoitem__cantidad'))
			aux1 = item.objects.filter(salidaitem__encsalidaitem__fecha__range=(f1, f2)).distinct().order_by('codigo').annotate(total=Sum('salidaitem__cantidad'))
			aux2 = item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).distinct().order_by('codigo').annotate(total=Sum('ingresoitem__sub_total'))
			aux3 = item.objects.filter(salidaitem__encsalidaitem__fecha__range=(f1, f2)).distinct().order_by('codigo').annotate(total=Sum('salidaitem__sub_total'))
	
			for q in aux_a:
				cantidad_e_a.append(q.total)
	
			if aux1_a:
				for i in aux_a:
					cont = 0
					if i in aux1_a:
						cantidad_s_a.append(aux1_a[cont].total)
						cont+=1
					else:
						cantidad_s_a.append(0)
			
			else:
				for i in aux_a:
					cantidad_s_a.append(0)
	
	
			for x in aux2_a:
				sub_total_e_a.append(x.total)
	
			if aux3_a:
				cont1 = 0
				for i in aux2_a:
					if i in aux3_a:
						sub_total_s_a.append(aux3_a[cont1].total)
						cont1+=1
					else:
						sub_total_s_a.append(0)
			else:
				for i in aux2_a:
					sub_total_s_a.append(0)
			
			for r in resp:
				if r in resp_a:
					saldo_c_a.append(cantidad_e_a[d] - cantidad_s_a[d])
					saldo_sub_a.append(sub_total_e_a[d] - sub_total_s_a[d])
					d+=1
				else:
					saldo_c_a.append(0)
					saldo_sub_a.append(0)
	
			for i in saldo_sub_a:
				tot_saldo_a = tot_saldo_a + i
				
			for i in aux:
				cantidad_e.append(i.total)
	
			if aux1:
				cont2 = 0
				for i in aux:
					if i in aux1:
						cantidad_s.append(aux1[cont2].total)
						cont2+=1
					else:
						cantidad_s.append(0)
			else:
				for i in aux1:
					cantidad_s.append(0)
	
			for k in item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).distinct().order_by('codigo'):
				saldo_c.append(cantidad_e[b] - cantidad_s[b])
				b+=1
	
			for m in aux2:
				sub_total_e.append(m.total)
	
			if aux3:
				cont3 = 0
				for i in aux2:
					if i in aux3:
						sub_total_s.append(aux3[cont3].total)
						cont3+=1
					else:
						sub_total_s.append(0)
	
			else:
				for i in aux2:
					sub_total_s.append(0)
	
			for i in sub_total_e:
				tot_saldo_e = tot_saldo_e + i
	
			for i in sub_total_s:
				tot_saldo_s = tot_saldo_s + i
	
			for o in item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).distinct().order_by('codigo'):
				saldo_sub.append(sub_total_e[c] - sub_total_s[c])
				c+=1
	
			res = item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).distinct().order_by('codigo').annotate(total_cant_e=Sum('ingresoitem__cantidad'), total_sub_e=Sum('ingresoitem__sub_total'))
			res1 = item.objects.filter(salidaitem__encsalidaitem__fecha__range=(f1, f2)).distinct().order_by('codigo').annotate(total_cant_s=Sum('salidaitem__cantidad'), total_sub_s=Sum('salidaitem__sub_total'))
	
			if res1:
				x = 0
				for i in res:
					if i in res1:
						salida.append(res1[x])
						x+=1
					else:
						salida.append(0)
			else:
				for i in res:
					salida.append(0)
	
	
			for p in item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).distinct().order_by('codigo'):
				saldo_c_t.append(saldo_c[f] + saldo_c_a[f])
				saldo_sub_t.append(saldo_sub[f] + saldo_sub_a[f])
				f+=1
	
			for i in saldo_sub_t:
				tot_saldo = tot_saldo + i
	
			lista = zip(res, salida, saldo_c_t, saldo_sub_t, saldo_c_a, saldo_sub_a)
	
	
			context['res'] = lista
			context['total_a'] = tot_saldo_a
			context['total_e'] = tot_saldo_e
			context['total_s'] = tot_saldo_s
			context['total_saldo'] = tot_saldo
			context['fecha1'] = fecha1
			context['fecha2'] = fecha2
			context['fecha3'] = fecha3

			return context

		except Exception as e:
			return None

class reporteKardexTemplate(FormView):
	form_class = repGeneralForm
	template_name = 'almacen/reporte_general.html'
	def get_context_data(self, **kwargs):
		context = super(reporteKardexTemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class reporteGeneral(PDFTemplateView):
	template_name = "almacen/rep_gral.html"
	def get_context_data(self, **kwargs):
		context = super(reporteGeneral, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		campo2 = self.request.GET.get('campo2')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		f3 = f1 - datetime.timedelta(days=1)
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		fecha3 = f3.strftime("%d/%m/%Y")
		
		if campo2 == 'T':
			res = item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).distinct().order_by('codigo')
		else:
			res = item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2), categoria=campo2).distinct().order_by('codigo')

		context['res'] = res
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2
		context['fecha3'] = fecha3
		context['f1'] = f1
		context['f2'] = f2
		context['f3'] = f3
		context['cat'] = campo2
		
		return context

class ResumenEySTemplate(FormView):
	form_class = repResumenEySForm
	template_name = 'almacen/resumen_eys.html'
	def get_context_data(self, **kwargs):
		context = super(ResumenEySTemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class reporteResumenEyS(PDFTemplateView):
	template_name = "almacen/reporte_resumen_eys.html"
	def get_context_data(self, **kwargs):
		context = super(reporteResumenEyS, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		campo2 = self.request.GET.get('campo2')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		
		if campo2 == 'E':
			res = encingresoitem.objects.filter(fecha__range=(f1, f2)).order_by('id')
			sumas = encingresoitem.objects.filter(fecha__range=(f1, f2)).aggregate(total_i=Sum('total_iva'), total_imp_i=Sum('importe_iva'), total=Sum('total'))
			context['total_i'] = sumas['total_i']
			context['total_imp_i'] = sumas['total_imp_i']
			context['total'] = sumas['total']
		else:
			res = encsalidaitem.objects.filter(fecha__range=(f1, f2)).order_by('id')
			sumas_s = encsalidaitem.objects.filter(fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
			context['total_s'] = sumas_s['total']

		context['res'] = res
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2
		context['f1'] = f1
		context['f2'] = f2
		context['tipo_mov'] = campo2
		
		return context

class DetalleEntradasTemplate(FormView):
	form_class = repDetalleEntradasForm
	template_name = 'almacen/detalle_entradas.html'
	def get_context_data(self, **kwargs):
		context = super(DetalleEntradasTemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class reporteDetalleEntradas(PDFTemplateView):
	template_name = "almacen/reporte_detalle_entradas.html"
	def get_context_data(self, **kwargs):
		context = super(reporteDetalleEntradas, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		campo2 = self.request.GET.get('campo2')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		
		if campo2 == 'T':
			res = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2)).order_by('encingresoitem__id')
			sumas = encingresoitem.objects.filter(fecha__range=(f1, f2)).aggregate(total_i=Sum('total_iva'), total_imp_i=Sum('importe_iva'), total=Sum('total'))
			context['total_i'] = sumas['total_i']
			context['total_imp_i'] = sumas['total_imp_i']
			context['total'] = sumas['total']
		else:
			res = item.objects.filter(ingresoitem__encingresoitem__fecha__range=(f1, f2)).distinct().order_by('codigo')
			sumas = encingresoitem.objects.filter(fecha__range=(f1, f2)).aggregate(total_cant=Sum('ingresoitem__cantidad'), total_i=Sum('total_iva'), total_imp_i=Sum('importe_iva'), total=Sum('total'))
			context['total_cant'] = sumas['total_cant']
			context['total_i'] = sumas['total_i']
			context['total_imp_i'] = sumas['total_imp_i']
			context['total'] = sumas['total']

		context['res'] = res
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2
		context['f1'] = f1
		context['f2'] = f2
		context['tipo_mov'] = campo2
		
		return context

class DetalleSalidasTemplate(FormView):
	form_class = repDetalleSalidasForm
	template_name = 'almacen/detalle_salidas.html'
	def get_context_data(self, **kwargs):
		context = super(DetalleSalidasTemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class reporteDetalleSalidas(PDFTemplateView):
	template_name = "almacen/reporte_detalle_salidas.html"
	def get_context_data(self, **kwargs):
		context = super(reporteDetalleSalidas, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		campo2 = self.request.GET.get('campo2')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		
		if campo2 == 'T':
			res = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2)).order_by('encsalidaitem__id')
			sumas = encsalidaitem.objects.filter(fecha__range=(f1, f2)).aggregate(total=Sum('salidaitem__sub_total'))
			context['total'] = sumas['total']
		else:
			res = item.objects.filter(salidaitem__encsalidaitem__fecha__range=(f1, f2)).distinct().order_by('codigo')
			sumas = encsalidaitem.objects.filter(fecha__range=(f1, f2)).aggregate(total_cant=Sum('salidaitem__cantidad'), total=Sum('salidaitem__sub_total'))
			context['total_cant'] = sumas['total_cant']
			context['total'] = sumas['total']

		context['res'] = res
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2
		context['f1'] = f1
		context['f2'] = f2
		context['tipo_mov'] = campo2
		
		return context

class DetalleClientesTemplate(FormView):
	form_class = repDetalleClienteForm
	template_name = 'almacen/detalle_clientes.html'
	def get_context_data(self, **kwargs):
		context = super(DetalleClientesTemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class reporteDetalleClientes(PDFTemplateView):
	template_name = "almacen/reporte_detalle_clientes.html"
	def get_context_data(self, **kwargs):
		context = super(reporteDetalleClientes, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		campo2 = self.request.GET.get('campo2')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		
		if campo2 == 'T':
			res = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2)).distinct().order_by('encsalidaitem__id')
			sumas = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2)).aggregate(total_cant=Sum('cantidad'), total_costo_u=Sum('costo_unit'), total=Sum('sub_total'))
		else:
			res = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2), encsalidaitem__cliente=campo2).distinct().order_by('encsalidaitem__id')
			sumas = salidaitem.objects.filter(encsalidaitem__fecha__range=(f1, f2), encsalidaitem__cliente=campo2).aggregate(total_cant=Sum('cantidad'), total_costo_u=Sum('costo_unit'), total=Sum('sub_total'))

		context['total_cant'] = sumas['total_cant']
		context['total_costo_u'] = sumas['total_costo_u']
		context['total'] = sumas['total']
		context['res'] = res
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2
		context['f1'] = f1
		context['f2'] = f2
		context['tipo_mov'] = campo2
		
		return context

class DetalleProveedoresTemplate(FormView):
	form_class = repDetalleProveedorForm
	template_name = 'almacen/detalle_proveedores.html'
	def get_context_data(self, **kwargs):
		context = super(DetalleProveedoresTemplate, self).get_context_data(**kwargs)
		if 'form'in context:
			context['form'] = self.form_class()
		return context

class reporteDetalleProveedores(PDFTemplateView):
	template_name = "almacen/reporte_detalle_proveedores.html"
	def get_context_data(self, **kwargs):
		context = super(reporteDetalleProveedores, self).get_context_data(**kwargs)
		campo = self.request.GET.get('campo')
		campo1 = self.request.GET.get('campo1')
		campo2 = self.request.GET.get('campo2')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		f2 = datetime.datetime.strptime(campo1, "%Y-%m-%d")
		fecha1 = f1.strftime("%d/%m/%Y")
		fecha2 = f2.strftime("%d/%m/%Y")
		
		if campo2 == 'T':
			res = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2)).distinct().order_by('encingresoitem__id')
			sumas = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2)).aggregate(total_cant=Sum('cantidad'), total_costo_u=Sum('costo_unit'), total=Sum('sub_total'))
		else:
			res = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2), encingresoitem__proveedor=campo2).distinct().order_by('encingresoitem__id')
			sumas = ingresoitem.objects.filter(encingresoitem__fecha__range=(f1, f2), encingresoitem__proveedor=campo2).aggregate(total_cant=Sum('cantidad'), total_costo_u=Sum('costo_unit'), total=Sum('sub_total'))

		context['total_cant'] = sumas['total_cant']
		context['total_costo_u'] = sumas['total_costo_u']
		context['total'] = sumas['total']
		context['res'] = res
		context['fecha1'] = fecha1
		context['fecha2'] = fecha2
		context['f1'] = f1
		context['f2'] = f2
		context['tipo_mov'] = campo2
		
		return context

class uploadCotizacionTC(FormView):
	form_class = XlsInputForm
	success_url = reverse_lazy('contabilidad:listacotizacion_tc')
	template_name = 'contabilidad/cotizacion_tcupload.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return self.render_to_response({'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			input_excel = request.FILES['input_excel']
			book = xlrd.open_workbook(file_contents=input_excel.read())
			sheet = book.sheets()[0]
			aux = []
			for i in range(0, sheet.nrows):
				f = sheet.cell_value(i, 0)
				f1 = datetime.datetime(*xlrd.xldate_as_tuple(f, book.datemode))
				f2 = f1.strftime("%Y-%m-%d")
				aux.append(f2)
			t_c = sheet.col_values(1, 0)
			u = sheet.col_values(2, 0)
			for fecha, tipo_c, ufv in zip(aux, t_c, u):
				cotizacion, created = Cotizacion.objects.get_or_create(fecha=fecha, tipo_c=tipo_c, ufv=ufv)
				cotizacion.save()
			return HttpResponseRedirect(self.success_url)
		else:
			return render(request, {'form':form})

#Actualización de inventarios
class actualizarInventario(FormView):
	form_class = actualizarInventarioForm
	success_url = reverse_lazy('almacenes:listasalida')
	template_name = 'almacen/act_inventario.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return self.render_to_response({'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		campo = self.request.POST.get('campo')
		f1 = datetime.datetime.strptime(campo, "%Y-%m-%d")
		if form.is_valid():
			ingreso = ingresoitem.objects.filter(encingresoitem__fecha__lte=f1)
			for i in ingreso:
				fecha = i.encingresoitem.fecha
				ufv_p = Cotizacion.objects.get(fecha=fecha).ufv
				ufv_u = Cotizacion.objects.get(fecha=f1).ufv
				u = ufv_u/ufv_p
				ufv = round(u, 7)
				aux1 = i.costo_unit * Decimal(ufv)
				aux2 = i.sub_total * Decimal(ufv)
				res = round(aux1, 2)
				res1 = round(aux2, 2)
				ingresoitem.objects.filter(encingresoitem__fecha__lte=f1, id=i.id).update(costo_unit_actualizado=res, sub_total_actualizado=res1)
			return HttpResponseRedirect(self.success_url)
		else:
			return render(request, {'form':form})












































































































"""
class crearInsumoAlmacen(CreateView):
	form_class = crearInsumoForm
	template_name = 'almacen/nuevoinsumo.html'
	success_url = reverse_lazy('almacenes:listainsumos')

class updateInsumo(UpdateView):
	model = insumos
	form_class = crearInsumoForm
	template_name = 'almacen/nuevoinsumo.html'
	success_url = reverse_lazy('almacenes:listainsumos')

class listaInsumos(CreateView,ListView):
	model = insumos
	form_class = searchForm
	template_name = 'almacen/listainsumos.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaInsumos, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearHerramientas(CreateView):
	form_class = crearHerramientasForm
	template_name = 'almacen/nuevaherramienta.html'
	success_url = reverse_lazy('almacenes:listaherramientas')

class updateHerramientas(UpdateView):
	model = herramientas
	form_class = crearHerramientasForm
	template_name = 'almacen/nuevaherramienta.html'
	success_url = reverse_lazy('almacenes:listaherramientas')

class listaHerramientas(CreateView,ListView):
	model = herramientas
	form_class = searchForm
	template_name = 'almacen/listaherramientas.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaHerramientas, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearMaquinariaEquipo(CreateView):
	form_class = crearMaquinariaEquipoForm
	template_name = 'almacen/crearmaquinariaequipo.html'
	success_url = reverse_lazy('almacenes:listamaquinariaequipo')

class updateMaquinariaEquipo(UpdateView):
	model = maquinaria_equipo
	form_class = crearMaquinariaEquipoForm
	template_name = 'almacen/nuevaherramienta.html'
	success_url = reverse_lazy('almacenes:listamaquinariaequipo')

class listaMaquinariaEquipo(CreateView,ListView):
	model = maquinaria_equipo
	form_class = searchForm
	template_name = 'almacen/listamaquinariaequipo.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaMaquinariaEquipo, self).get_context_data(**kwargs)	
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class listaItemsPedidos(CreateView,ListView):
	model = item
	form_class = searchForm
	template_name = 'almacen/listaitemspedeido.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaItemsPedidos, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		ct=self.kwargs['ct']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(proyecto__ubicacion_proyecto=ct,id = id)
		else:
			object_list = self.model.objects.filter(proyecto__ubicacion_proyecto=ct).order_by('id')
		return object_list

class ingresoInsumoItem(CreateView):
	model_pk = item
	form_class = crearIngresoInsumoForm
	template_name = 'almacen/crearingresoinsumo.html'
	success_url = 'almacenes:listaingresoinsumo'

	def get_context_data(self, **kwargs):
		context = super (ingresoInsumoItem, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
			context['item'] = item.objects.get(id=pk1)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			pk1=self.kwargs['pk']
			form =form.save(commit=False)
			form.item = self.model_pk.objects.get(id=pk1)
			form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			form.save()
			a=insumosAlmacen.objects.get_or_create(almacen=form.almacen,insumos=form.insumos)
			a[0].cantidad = a[0].cantidad + form.cantidad
			a[0].save()
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaIngresoInsumoItem(CreateView,ListView):
	model = ingresoInsumos
	form_class = searchForm
	template_name = 'almacen/listaingresoinsumoitem.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaIngresoInsumoItem, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
			context['item'] = item.objects.get(id=pk1)
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class salidaInsumoItem(CreateView):
	model_pk = item
	form_class = crearSalidaInsumoForm
	template_name = 'almacen/salidainsumo.html'
	success_url = 'almacenes:listasalidainsumo'

	def get_context_data(self, **kwargs):
		context = super (salidaInsumoItem, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
			context['item'] = item.objects.get(id=pk1)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			from django.db.models import Sum
			pk1=self.kwargs['pk']
			#form =form.save(commit=False)
			#almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			almacen_obj = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			aux = ingresoInsumos.objects.filter(item=pk1 ,insumos=form.cleaned_data['insumos'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			aux1 = salidaInsumos.objects.filter(item=pk1 ,insumos=form.cleaned_data['insumos'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			total_ing = aux['cantidad__sum']
			#print(total_ing)
			total_sali = aux1['cantidad__sum']
			#print(total_sali)
			if(aux['cantidad__sum'] is None):
				total_ing = 0
			if(aux1['cantidad__sum'] is None):
				total_sali = 0	 
			total = total_ing - total_sali

			if(aux['cantidad__sum'] is None):
				return self.render_to_response(self.get_context_data(form=form,error='No se tiene ingresos de este insumo para el item'))
			if(form.cleaned_data['cantidad']>total):
				return self.render_to_response(self.get_context_data(form=form,error='La cantidad exede el stock actual de '+ str(total)))
			else:
				form =form.save(commit=False)
				#print(almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto))
				form.item = self.model_pk.objects.get(id=pk1)
				form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
				form.save()
				a=insumosAlmacen.objects.get(almacen=form.almacen,insumos=form.insumos)
				a.cantidad = a.cantidad - form.cantidad
				a.save()
				return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaSalidaInsumo(CreateView,ListView):
	model = salidaInsumos
	form_class = searchForm
	template_name = 'almacen/listasalidainsumo.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super (listaSalidaInsumo, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' in context:
			context['form'] = self.form_class()
			context['item'] = item.objects.get(id=pk1)
		return context

	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class ingresoHerramientasView(CreateView):
	model_pk = almacen
	form_class = crearIngresoHerramientasForm
	template_name = 'almacen/ingresoherramientas.html'
	success_url = reverse_lazy('almacenes:listaalmacenes')

	def get_context_data(self, **kwargs):
		context = super (ingresoHerramientasView, self).get_context_data(**kwargs)
		ct = self.kwargs['ct']
		if 'form' and 'ct' not in context:
			context['form'] = self.form_class()
			context['ct'] = almacen.objects.get(ciudad=ct)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			ct=self.kwargs['ct']
			#print(ct)
			form =form.save(commit=False)
			#print(self.model_pk.objects.get(ciudad=ct))
			form.almacen = self.model_pk.objects.get(ciudad=ct)
			form.save()
			a=herramientasAlmacen.objects.get_or_create(almacen=form.almacen,herramientas=form.herramientas)
			a[0].cantidad = a[0].cantidad + form.cantidad
			a[0].save()

			return  HttpResponseRedirect(self.success_url)
		else:
			return self.render_to_response(self.get_context_data(form=form))

class salidaHerramientasView(CreateView):
	model_pk = item
	form_class = crearSalidaHerramientasForm
	template_name = 'almacen/salidaherramientas.html'
	success_url = 'almacenes:listasalidaherramientas'

	def get_context_data(self, **kwargs):
		context = super (salidaHerramientasView, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
			context['item'] = item.objects.get(id=pk1)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			from django.db.models import Sum
			pk1=self.kwargs['pk']
			#form =form.save(commit=False)
			#almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)

			almacen_obj = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			aux = ingresoHerramientas.objects.filter(herramientas=form.cleaned_data['herramientas'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			aux1 = salidaHerramientas.objects.filter(herramientas=form.cleaned_data['herramientas'],almacen=almacen_obj,debuelto=False).aggregate(Sum('cantidad'))

			total_ing = aux['cantidad__sum']
			#print(total_ing)
			total_sali = aux1['cantidad__sum']
			#print(total_sali)
			
			if(aux['cantidad__sum'] is None):
				total_ing = 0
			if(aux1['cantidad__sum'] is None):
				total_sali = 0	 
			total = total_ing - total_sali
			print(total)

			if(aux['cantidad__sum'] is None):
				return self.render_to_response(self.get_context_data(form=form,error='No se tiene ingresos de este herramientas para el item'))

			if(form.cleaned_data['cantidad']>total):
				return self.render_to_response(self.get_context_data(form=form,error='La cantidad exede el stock actual de '+ str(total)))

			else:
				form =form.save(commit=False)
				#print(almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto))
				form.item = self.model_pk.objects.get(id=pk1)
				form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
				form.save()
				a=herramientasAlmacen.objects.get(almacen=form.almacen,herramientas=form.herramientas)
				a.cantidad = a.cantidad - form.cantidad
				a.save()
			
				return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaSalidaHerramientas(CreateView,ListView):
	model = salidaHerramientas
	form_class = searchForm
	template_name = 'almacen/listasalidaherramientas.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super (listaSalidaHerramientas, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
			context['item'] = item.objects.get(id=pk1)
		return context

	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class ingresoMaquinariaEquipo(CreateView):
	model_pk = almacen
	form_class = crearIngresoMaquinariaEquipoForm
	template_name = 'almacen/ingresomaquinariaequipo.html'
	success_url = reverse_lazy('almacenes:listaalmacenes')

	def get_context_data(self, **kwargs):
		context = super (ingresoMaquinariaEquipo, self).get_context_data(**kwargs)
		ct = self.kwargs['ct']
		if 'form' and 'ct' not in context:
			context['form'] = self.form_class()
			context['ct'] = almacen.objects.get(ciudad=ct)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			ct=self.kwargs['ct']
			#print(ct)
			form =form.save(commit=False)
			#print(self.model_pk.objects.get(ciudad=ct))
			form.almacen = self.model_pk.objects.get(ciudad=ct)
			form.save()
			a=maquinaria_equipoAlmacen.objects.get_or_create(almacen=form.almacen,maquinaria_equipo=form.maquinaria_equipo)
			a[0].cantidad = a[0].cantidad + form.cantidad
			a[0].save()

			return  HttpResponseRedirect(self.success_url)
		else:
			return self.render_to_response(self.get_context_data(form=form))

class salidaMaquinariaEquipo(CreateView):
	model_pk = item
	form_class = crearSalidaMaquinariaEquipoForm
	template_name = 'almacen/salidamaquinariaequipo.html'
	success_url = 'almacenes:listasalidamaquinariaequipo'

	def get_context_data(self, **kwargs):
		context = super (salidaMaquinariaEquipo, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
			context['item'] = item.objects.get(id=pk1)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid():
			from django.db.models import Sum
			pk1=self.kwargs['pk']
			#form =form.save(commit=False)
			#almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)

			almacen_obj = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
			aux = ingresoMaquinaria_equipo.objects.filter(maquinaria_equipo=form.cleaned_data['maquinaria_equipo'],almacen=almacen_obj).aggregate(Sum('cantidad'))
			aux1 = salidaMaquinaria_equipo.objects.filter(maquinaria_equipo=form.cleaned_data['maquinaria_equipo'],almacen=almacen_obj,debuelto=False).aggregate(Sum('cantidad'))

			total_ing = aux['cantidad__sum']
			#print(total_ing)
			total_sali = aux1['cantidad__sum']
			#print(total_sali)
			
			if(aux['cantidad__sum'] is None):
				total_ing = 0
			if(aux1['cantidad__sum'] is None):
				total_sali = 0	 
			total = total_ing - total_sali
			#print(total)
		
			if(aux['cantidad__sum'] is None):
				return self.render_to_response(self.get_context_data(form=form,error='No se tiene ingresos de este herramientas para el item'))

			if(form.cleaned_data['cantidad']>total):
				return self.render_to_response(self.get_context_data(form=form,error='La cantidad exede el stock actual de '+ str(total)))

			else:
				form =form.save(commit=False)
				#print(almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto))
				form.item = self.model_pk.objects.get(id=pk1)
				form.almacen = almacen.objects.get(ciudad=self.model_pk.objects.get(id=pk1).proyecto.ubicacion_proyecto)
				form.save()
				a=maquinaria_equipoAlmacen.objects.get(almacen=form.almacen,maquinaria_equipo=form.maquinaria_equipo)
				a.cantidad = a.cantidad - form.cantidad
				a.save()
			
				return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'pk': pk1}))

		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaSalidaMaquinariaEquipo(CreateView,ListView):
	model = salidaMaquinaria_equipo
	form_class = searchForm
	template_name = 'almacen/listasalidamaquinariaequipo.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super (listaSalidaMaquinariaEquipo, self).get_context_data(**kwargs)
		pk1=self.kwargs['pk']
		if 'form' and 'item' not in context:
			context['form'] = self.form_class()
			context['item'] = item.objects.get(id=pk1)
		return context

	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		pk=self.kwargs['pk']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item=item.objects.get(id=pk),id = id)
		else:
			object_list = self.model.objects.filter(item=item.objects.get(id=pk)).order_by('id')
		return object_list

class listaConfirmacionHerramientas(CreateView,ListView):
	model = salidaHerramientas
	form_class = searchForm
	template_name = 'almacen/listaConfirmacionHerramientas.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super (listaConfirmacionHerramientas, self).get_context_data(**kwargs)
		ct = self.kwargs['ct']
		if 'form' and 'ct' not in context:
			context['form'] = self.form_class()
			context['ct'] = almacen.objects.get(ciudad=ct)
		return context

	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		ct=self.kwargs['ct']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item__proyecto__ubicacion_proyecto=ct, debuelto=False, id = id)
		else:
			object_list = self.model.objects.filter(item__proyecto__ubicacion_proyecto=ct, debuelto=False).order_by('id')
		return object_list

class debolucionHerramientas(UpdateView):
	model = salidaHerramientas
	form_class = crearDebolucionHerramientas
	template_name = 'almacen/nuevaherramienta_dev.html'
	success_url = 'almacenes:listaconfirmacionherramientas'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)

		form = self.form_class(request.POST,instance=modelRes)

		if form.is_valid():
			print (form)
			form =form.save(commit=False)
			if(form.debuelto):

				a = herramientasAlmacen.objects.get(almacen=form.almacen,herramientas=form.herramientas)
				
				ct = a.almacen.ciudad
				
				a.cantidad = a.cantidad + form.cantidad
				a.save()
				form.save()
				print (a)
				print ("paso")
				
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'ct': ct}))
		else:
			print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class listaConfirmacionMaquinariaHequipo(CreateView,ListView):
	model = salidaMaquinaria_equipo
	form_class = searchForm
	template_name = 'almacen/listaConfirmacionMaquinariaHequipo.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super (listaConfirmacionMaquinariaHequipo, self).get_context_data(**kwargs)
		ct = self.kwargs['ct']
		if 'form' and 'ct' not in context:
			context['form'] = self.form_class()
			context['ct'] = almacen.objects.get(ciudad=ct)
		return context

	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		ct=self.kwargs['ct']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(item__proyecto__ubicacion_proyecto=ct, debuelto=False, id = id)
		else:
			object_list = self.model.objects.filter(item__proyecto__ubicacion_proyecto=ct, debuelto=False).order_by('id')
		return object_list

class debolucionMaquinariaHequipo(UpdateView):
	model = salidaMaquinaria_equipo
	form_class = crearDebolucionMaquinariaEquipo
	template_name = 'almacen/nuevamaquinaria_dev.html'
	success_url = 'almacenes:listaconfirmacionmaquinariahequipo'
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)

		form = self.form_class(request.POST,instance=modelRes)

		if form.is_valid():
			print (form)
			form =form.save(commit=False)
			

			a = maquinaria_equipoAlmacen.objects.get(almacen=form.almacen,maquinaria_equipo=form.maquinaria_equipo)
			ct = a.almacen.ciudad
			if(form.debuelto):
				a.cantidad = a.cantidad + form.cantidad
				a.save()
				form.save()
				print (a)
				#print ("paso")
			
			return  HttpResponseRedirect(reverse_lazy(self.success_url, kwargs = {'ct': ct}))
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class crearTipoActivo(CreateView):
	form_class = crearTipoActivoForm
	template_name ='almacen/creartipoactivo.html'
	success_url = "/"
	
class crearActivo(CreateView):
	form_class = crearActivoForm
	template_name ='almacen/crearactivo.html'
	success_url = reverse_lazy('almacenes:listacrearactivo')

class updateActivo(UpdateView):
	model = activo
	form_class = crearActivoForm
	template_name ='almacen/crearactivo_up.html'
	success_url = reverse_lazy('almacenes:listacrearactivo')

class listaCrearActivo(CreateView,ListView):
	model = activo
	form_class = searchForm
	template_name = 'almacen/listaactivo.html'
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super (listaCrearActivo, self).get_context_data(**kwargs)
		if 'form' in context:
			context['form'] = self.form_class()
		return context
	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class()
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list , form=form))
	def get_queryset(self):
		#ct=self.kwargs['ct']
		id = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				print(self.request.GET)
				print(form)
				id = form.cleaned_data['search']
				#kwargs['id']
				print(id)
		if (id):
			#object_list = self.model.objects.filter(name__icontains = id)
			object_list = self.model.objects.filter(id = id)
		else:
			object_list = self.model.objects.filter().order_by('id')
		return object_list

class crearActivoDepreciasion(CreateView):
	form_class = crearActivoForm
	template_name ='almacen/crearactivodepre.html'
	success_url = "/"
	def get_context_data(self, **kwargs):
		context = super (crearActivoDepreciasion, self).get_context_data(**kwargs)
		import datetime
		datenow = datetime.datetime.now()

		pk=self.kwargs['pk']
		a = activo.objects.get(id=pk)

		act = datenow.year - a.fecha_ingreso.year
		dep = a.costo_total / a.tipoActivo.años_vida_util

		tdep = dep*act
		res= a.costo_total-tdep

		if 'form' not in context or 'res' not in context:
			context['form'] = self.form_class()
			context['res'] = res
		return context

def reporteAlmacen(request,ct):
	#consultas

	y,x=A4
	#construccion
	response = HttpResponse(content_type='application/pdf')
	#response['Content-Disposition'] = 'attachment; filename=reporte.pdf'
	response['Content-Disposition'] = 'filename=reporte.pdf'
	#response["Content-Disposition"] = "inline"
	buffer = BytesIO()

	c = canvas.Canvas(buffer,pagesize=A4)
	comienso = 750
	print(A4)
	#encavesado espacio abajo arriba 91
	c.setLineWidth(.3)
	c.setFont('Helvetica',22)
	c.drawCentredString(y/2,comienso,'Reporte de Almacen')

	#items

	c.save()
	pdf = buffer.getvalue()
	response.write(pdf)
	return response

class envio_reporte_material(PDFTemplateView):
	template_name = "almacen/envio_reporte_material.html"
	def get_context_data(self, **kwargs):
		context = super(envio_reporte_material, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		try:
			context['res'] = salidaMaterial.objects.get(pk=pk)
			context['usuario'] = self.request.user
		except:
			raise Http404
		return context
class envio_reporte_insumo(PDFTemplateView):
	template_name = "almacen/envio_reporte_insumo.html"
	def get_context_data(self, **kwargs):
		context = super(envio_reporte_insumo, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk')
		try:
			context['res'] = salidaInsumos.objects.get(pk=pk)
			context['usuario'] = self.request.user
		except:
			raise Http404
		return context
"""
