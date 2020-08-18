# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from usuarios.views import *
from django.contrib.auth.views import login, logout_then_login, password_reset
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import views as auth_views

from rest_framework import routers
from .serializers_views import *

router = routers.DefaultRouter()
router.register(r'currentuser', currentUserViewSetRest)

urlpatterns = [
	url(r'^restpersonal/', include(router.urls)),
    #login_required metodo de forsado de login
    url(r'^$', 
        login_required(main_page), 
        name='main'
    ),
    url(r'^nuevousuario/$',
        #aqui el decorador de permisos
        permission_required('auth.view_personal')(login_required(crearUsuario.as_view())), 
        name='nuevousuario'
    ),
    #url(r'^listausuario/(?P<id>\d*)/*$', login_required(listaUsuario.as_view()), name='listausuario'),
    url(r'^listausuario/$', 
        permission_required('auth.view_personal') (login_required(csrf_exempt(listaUsuario.as_view()))), 
        name='listausuario'
    ),
    url(r'^crearcargo/$', 
        permission_required('auth.view_personal') (login_required(crearCargo.as_view())), 
        name='crearcargo'
    ),
    url(r'^listacargo/$', 
        permission_required('auth.view_personal') (login_required(listaCargo.as_view())), 
        name='listacargo'
    ),
    url(r'^agregarpermisos/(?P<pk>\d+)/$',
        permission_required('auth.view_personal') (login_required(agregarPermisos.as_view())), 
        name='agregarpermisos'
    ),
    #actualisacion de cuenta por el usuario
  
    #login_required metodo de forsado de login, logout_then_login metodos de logeo de django
    url(r'^login/$',
        login,
        {'template_name':'personal/login.html'}, 
        name='login'
    ),
    url(r'^logout/$',
        logout_then_login,
        name='logout'
    ),
    url(r'^reset_pass/$',
        permission_required('auth.view_personal')(auth_views.password_change),
        {'template_name':'personal/password_reset_form.html','post_change_redirect' : '/'}, 
        name='reset_password'
    ),
    url(r'^updateusuario/(?P<pk>\d+)/$',
        permission_required('auth.view_personal')(login_required(updateUsuario.as_view())), 
        name='updateusuario'
    ),

    url(r'^updateusuario_user/$', 
        permission_required('auth.view_personal')(login_required(updateUsuarioFronUser.as_view())), 
        name='updateusuariofronuser'
    ),
    url(r'^darbaja/(?P<pk>\d+)/$', 
        permission_required('auth.view_personal')(login_required(updateDarBaja.as_view())), 
        name='updatedarbaja'
    ),
    url(r'^updatecargo/(?P<pk>\d+)/$', 
        permission_required('auth.view_personal')(login_required(updateCargo.as_view())), 
        name='updatecargo'
    ),
    url(r'^nuevopersonal/$',
        permission_required('auth.view_personal')(login_required(crearPersonal.as_view())), 
        name='nuevopersonal'
    ),
    url(r'^listapersonal/$',
        permission_required('auth.view_personal')(login_required(listaPersonal.as_view())), 
        name='listapersonal'
    ),
    url(r'^updatepersonal/(?P<pk>\d+)/$',
        permission_required('auth.view_personal')(login_required(updatePersonal.as_view())), 
        name='updatepersonal'
    ),
  
]