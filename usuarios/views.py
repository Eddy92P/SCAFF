# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.views.generic.edit import FormMixin
from django.http import Http404
from django.utils.translation import ugettext as _

from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from usuarios.forms import *
from usuarios.models import *
from django.contrib.auth.models import User

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType




def main_page(request):
	return render (request,"base/index.html",{})

class crearUsuario(CreateView):
	form_class = crearUsuarioUserForm
	second_form_class = crearKardexUsuarioForm
	template_name = 'personal/nuevousuario.html'
	success_url = reverse_lazy('personal:listausuario')
	def get_context_data(self, **kwargs):
		context = super(crearUsuario, self).get_context_data(**kwargs)
		if 'form' not in context or 'form2' not in context:
			context['form'] = self.form_class()
			context['form2'] = self.second_form_class()
		return context
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			form2save = form2.save(commit=False)
			form2save.user = form.save()
			form2save.save()
			return HttpResponseRedirect(self.success_url)
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

class updateUsuario(UpdateView):
	model = User
	second_model = kardex
	form_class = updateUsuarioUserForm
	second_form_class = crearKardexUsuarioForm
	template_name = 'personal/nuevousuario_edit.html'
	succes_url = reverse_lazy('personal:listausuario')
	def get_context_data(self, **kwargs):
		context = super(updateUsuario, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)
		#modelRes2 = self.second_model.objects.get(id=modelRes.id)
		modelRes2 = self.second_model.objects.get(user=modelRes)
		if 'form' not in context or 'form2' not in context:
			context['form'] = self.form_class(instance=modelRes)
			context['form2'] = self.second_form_class(instance=modelRes2)
			print(context)
		return context
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		pk = self.kwargs.get('pk',0)
		modelRes = self.model.objects.get(id=pk)
		modelRes2 = self.second_model.objects.get(user=modelRes)

		form = self.form_class(request.POST,instance=modelRes)
		form2 = self.second_form_class(request.POST,request.FILES, instance=modelRes2)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid() and form2.is_valid():
			#print ("paso")
			form2Save = form2.save(commit=False)
			form2Save.user = form.save()
			form2Save.save()
			return  HttpResponseRedirect(self.succes_url)
		else:
			#print ("paso2")
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

#actualisa datos del usuario actual logeado
class updateUsuarioFronUser(UpdateView):
	model = kardex
	form_class = crearModificarKardexForm
	template_name = 'personal/updatefromuser.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(updateUsuarioFronUser, self).get_context_data(**kwargs)
		pk = self.request.user.id
		modelRes = self.model.objects.get(user=self.request.user)
		if 'form' not in context:
			context['form'] = self.form_class(instance=modelRes)
		if 'uss' not in context:
			context['uss'] = self.get_object()
		return context

	def get_object(self):
		return self.model.objects.get(user=self.request.user)

class updateDarBaja(UpdateView):
	model = User
	form_class = darBajaForm
	template_name = 'personal/baja.html'
	success_url = reverse_lazy('personal:listausuario')
	def get_context_data(self, **kwargs):
		context = super(updateDarBaja, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		user = self.model.objects.get(id=pk)
		if 'form' and 'user' not in context :
			context['form'] = self.form_class()
			context['user'] = user
		return context
class listaUsuario(CreateView, ListView):
	model = User
	form_class = searchForm
	template_name = 'personal/listausuario.html'
	paginate_by = 15

	def get(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.GET)
		if request.GET:
			form = self.form_class(request.GET)
		self.object_list = self.get_queryset()
		return self.render_to_response(self.get_context_data(object_list=self.object_list, form=form))

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
			object_list = self.model.objects.filter(id = id, is_staff=False)
		else:
			object_list = self.model.objects.all().filter(is_staff=False).order_by('id')
		return object_list
class agregarPermisos(FormView):
	model = User
	form_class = addPermissionsForm
	template_name = 'personal/agregarpermisos.html'
	succes_url = reverse_lazy('personal:listausuario')

	def get_context_data(self, **kwargs):
		context = super(agregarPermisos, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		user = self.model.objects.get(id=pk)
		form = self.form_class(initial={'mod_personal':user.has_perm('auth.view_personal'),
										'mod_contabilidad':user.has_perm('auth.view_contabilidad'),
										'mod_almacenes':user.has_perm('auth.view_almacenes'),
										'mod_activos_f':user.has_perm('auth.view_activos_f')})
		#form.fields["mod_personal"] = True
		#print(form)
		if 'form' in context :
			context['form'] = form
			context['user'] = user
		return context
	def post(self, request, *args, **kwargs):
		#self.object = self.get_object	
		form = self.form_class(request.POST)
		pk = self.kwargs.get('pk',0)
		my_user = self.model.objects.get(id=pk)
		if form.is_valid():
			content_type = ContentType.objects.get_for_model(self.model)
			permission = Permission.objects.get(content_type=content_type, codename='view_personal')
			if(form.cleaned_data['mod_personal']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
			permission = Permission.objects.get(content_type=content_type, codename='view_contabilidad')
			if(form.cleaned_data['mod_contabilidad']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
			permission = Permission.objects.get(content_type=content_type, codename='view_cargas')
			if(form.cleaned_data['mod_cargas']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
		

			return  HttpResponseRedirect(self.succes_url)
		else:
			print ("paso2")
			return self.render_to_response(self.get_context_data(form=form))

class crearCargo(CreateView):
	form_class = cargoForm
	template_name = 'personal/nuevocargo.html'
	success_url = reverse_lazy('personal:listacargo')

class listaCargo(CreateView,ListView):
	model = cargo
	form_class = searchForm
	template_name = 'personal/listacargo.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super (listaCargo, self).get_context_data(**kwargs)
		if 'form' not in context:
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
			object_list = self.model.objects.filter(pk=id)
		else:
			object_list = self.model.objects.all().filter().order_by('id')
		return object_list

class updateCargo(UpdateView):
	model = cargo
	form_class = cargoForm
	template_name = 'personal/nuevocargo_edit.html'
	success_url = reverse_lazy('personal:listacargo')

class crearPersonal(CreateView):
	form_class = crearPersonalForm
	template_name = 'personal/nuevopersonal.html'
	success_url = reverse_lazy('personal:listapersonal')

class updatePersonal(UpdateView):
	model = personal
	form_class = crearPersonalForm
	template_name = 'personal/nuevopersonal.html'
	success_url = reverse_lazy('personal:listapersonal')

class listaPersonal(CreateView,ListView):
	model = personal
	form_class = searchForm
	template_name = 'personal/listapersonal.html'
	def get_context_data(self, **kwargs):
		context = super (listaPersonal, self).get_context_data(**kwargs)	
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