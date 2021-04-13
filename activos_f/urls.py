"""constructora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required

from almacenes.views import *
from contabilidad.views import *
from activos_f.views import *

from rest_framework import routers



router = routers.DefaultRouter()
"""router.register(r'materiales', materialesViewSetRest)
router.register(r'insumos', insumosViewSetRest)
router.register(r'salidainsumos', salidaInsumosSerializerRest)
router.register(r'salidamaterial', salidaMaterialSerializerRest)"""

urlpatterns = [
    #Autocompletado
    url(r'^asiento_autocomplete/$',
        permission_required('auth.view_activos_f')(login_required(asientoAutocomplete.as_view())), 
        name='asiento_autocomplete'
    ),
	url(r'^rubro_autocomplete/$',
        permission_required('auth.view_activos_f')(login_required(rubroAutocomplete.as_view())), 
        name='rubro_autocomplete'
    ),
    url(r'^tipo_bien_autocomplete/$',
        permission_required('auth.view_activos_f')(login_required(tipo_bienAutocomplete.as_view())), 
        name='tipo_bien_autocomplete'
    ),
    url(r'^personal_autocomplete/$',
        permission_required('auth.view_activos_f')(login_required(personalAutocomplete.as_view())), 
        name='personal_autocomplete'
    ),
    url(r'^ubicacion_autocomplete/$',
        permission_required('auth.view_activos_f')(login_required(ubicacionAutocomplete.as_view())), 
        name='ubicacion_autocomplete'
    ),

    #Urls
    url(r'^nuevorubro/$',
        permission_required('auth.view_activos_f')(login_required(crearRubro.as_view())), 
        name='nuevorubro'
    ),
    url(r'^listarubro/$',
        permission_required('auth.view_activos_f')(login_required(listaRubro.as_view())), 
        name='listarubro'
    ),
    url(r'^updaterubro/(?P<pk>\d+)/$',
        permission_required('auth.view_activos_f')(login_required(updateRubro.as_view())), 
        name='updaterubro'
    ),
    url(r'^nuevotipo_bien/$',
        permission_required('auth.view_activos_f')(login_required(crearTipo_bien.as_view())), 
        name='nuevotipo_bien'
    ),
    url(r'^listatipo_bien/$',
        permission_required('auth.view_activos_f')(login_required(listaTipo_bien.as_view())), 
        name='listatipo_bien'
    ),
    url(r'^updatetipo_bien/(?P<pk>\d+)/$',
        permission_required('auth.view_activos_f')(login_required(updateTipo_bien.as_view())), 
        name='updatetipo_bien'
    ),
    url(r'^nuevaubicacion/$',
        permission_required('auth.view_activos_f')(login_required(crearUbicacion.as_view())), 
        name='nuevaubicacion'
    ),
    url(r'^listaubicacion/$',
        permission_required('auth.view_activos_f')(login_required(listaUbicacion.as_view())), 
        name='listaubicacion'
    ),
    url(r'^updateubicacion/(?P<pk>\d+)/$',
        permission_required('auth.view_activos_f')(login_required(updateUbicacion.as_view())), 
        name='updateubicacion'
    ),
    url(r'^nueva_altaactivo/$',
        permission_required('auth.view_activos_f')(login_required(crearAltaActivo.as_view())), 
        name='nueva_altaactivo'
    ),
    url(r'^nueva_altaactivo/(?P<pk>\d+)/$',
        permission_required('auth.view_activos_f')(login_required(crearAltaActivo.as_view())), 
        name='nueva_altaactivo1'
    ),
    url(r'^update_altaactivo/(?P<pk>\d+)/$',
        permission_required('auth.view_activos_f')(login_required(updateAltaActivo.as_view())), 
        name='update_altaactivo'
    ),
    url(r'^lista_altaactivo/$',
        permission_required('auth.view_activos_f')(login_required(listaAltaActivo.as_view())), 
        name='lista_altaactivo'
    ),
    url(r'^update_bajaactivo/(?P<pk>\d+)/$',
        permission_required('auth.view_activos_f')(login_required(updateBajaActivo.as_view())), 
        name='update_bajaactivo'
    ),
    url(r'^lista_bajaactivo/$',
        permission_required('auth.view_activos_f')(login_required(listaBajaActivo.as_view())), 
        name='lista_bajaactivo'
    ),
    url(r'^nueva_capitalizacion/$',
        permission_required('auth.view_activos_f')(login_required(crearCapitalizacion.as_view())), 
        name='nueva_capitalizacion'
    ),
    url(r'^nueva_capitalizacion/(?P<pk>\d+)/$',
        permission_required('auth.view_activos_f')(login_required(crearCapitalizacion.as_view())), 
        name='nueva_capitalizacion1'
    ),
    url(r'^update_capitalizacion/(?P<pk>\d+)/$',
        permission_required('auth.view_activos_f')(login_required(updateCapitalizacion.as_view())), 
        name='update_capitalizacion'
    ),
    url(r'^lista_capitalizacion/$',
        permission_required('auth.view_activos_f')(login_required(listaCapitalizacion.as_view())), 
        name='lista_capitalizacion'
    ),
    url(r'^temp_espec_bien/$',
        permission_required('auth.view_activos_f')(login_required(ReporteEspecBienTemplate.as_view())), 
        name='temp_espec_bien'
    ),
    url(r'^reporte_espec_bien/$',
        permission_required('auth.view_activos_f')(login_required(ReporteEspecBien.as_view())), 
        name='reporte_espec_bien'
    ),
    url(r'^temp_alta_baja/$',
        permission_required('auth.view_activos_f')(login_required(ReporteAltaBajaTemplate.as_view())), 
        name='temp_alta_baja'
    ),
    url(r'^reporte_alta_baja/$',
        permission_required('auth.view_activos_f')(login_required(ReporteAltaBaja.as_view())), 
        name='reporte_alta_baja'
    ),
    url(r'^temp_inventario/$',
        permission_required('auth.view_activos_f')(login_required(ReporteInventarioTemplate.as_view())), 
        name='temp_inventario'
    ),
    url(r'^reporte_inventario/$',
        permission_required('auth.view_activos_f')(login_required(ReporteInventario.as_view())), 
        name='reporte_inventario'
    ),
    url(r'^temp_rep_especbien_excel/$',
        permission_required('auth.view_activos_f')(login_required(ReporteEspecBienExcelTemplate.as_view())), 
        name='temp_rep_especbien_excel'
    ),
    url(r'^rep_especbien_excel/$',
        permission_required('auth.view_activos_f')(login_required(ReporteEspecBienExcel.as_view())), 
        name='rep_especbien_excel'
    ),
    url(r'^temp_rep_altabaja_excel/$',
        permission_required('auth.view_activos_f')(login_required(ReporteAltaBajaTemplateExcel.as_view())), 
        name='temp_rep_altabaja_excel'
    ),
    url(r'^rep_altabaja_excel/$',
        permission_required('auth.view_activos_f')(login_required(ReporteAltaBajaExcel.as_view())), 
        name='rep_altabaja_excel'
    ),
    url(r'^temp_rep_inventario_excel/$',
        permission_required('auth.view_activos_f')(login_required(ReporteInventarioTemplateExcel.as_view())), 
        name='temp_rep_inventario_excel'
    ),
    url(r'^rep_inventario_excel/$',
        permission_required('auth.view_activos_f')(login_required(ReporteInventarioExcel.as_view())),
        name='rep_inventario_excel'
    ),
]