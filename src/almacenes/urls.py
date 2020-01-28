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

from rest_framework import routers
from .serializers_views import *


router = routers.DefaultRouter()
"""router.register(r'materiales', materialesViewSetRest)
router.register(r'insumos', insumosViewSetRest)
router.register(r'salidainsumos', salidaInsumosSerializerRest)
router.register(r'salidamaterial', salidaMaterialSerializerRest)"""

urlpatterns = [
    #url(r'^restalmacen/', include(router.urls)),
    #Ajax
    url(r'^nivel_uno_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(nivel_unoAutocomplete.as_view())), 
        name='nivel_uno_autocomplete'
    ),
    url(r'^nivel_dos_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(nivel_dosAutocomplete.as_view())), 
        name='nivel_dos_autocomplete'
    ),
    url(r'^nivel_tres_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(nivel_tresAutocomplete.as_view())), 
        name='nivel_tres_autocomplete'
    ),
    url(r'^nivel_cuatro_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(nivel_cuatroAutocomplete.as_view())), 
        name='nivel_cuatro_autocomplete'
    ),
    url(r'^asiento_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(asientoAutocomplete.as_view())), 
        name='asiento_autocomplete'
    ),
    url(r'^categoria_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(categoriaAutocomplete.as_view())), 
        name='categoria_autocomplete'
    ),
    url(r'^subcategoria_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(subcategoriaAutocomplete.as_view())), 
        name='subcategoria_autocomplete'
    ),
    url(r'^item_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(itemAutocomplete.as_view())), 
        name='item_autocomplete'
    ),
    url(r'^item_act_autocomplete/$',
        permission_required('auth.view_activos_f')(login_required(itemActAutocomplete.as_view())), 
        name='item_act_autocomplete'
    ),
    url(r'^personal_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(personalAutocomplete.as_view())), 
        name='personal_autocomplete'
    ),
    url(r'^proveedor_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(proveedorAutocomplete.as_view())), 
        name='proveedor_autocomplete'
    ),
    url(r'^cliente_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(clienteAutocomplete.as_view())), 
        name='cliente_autocomplete'
    ),
    url(r'^ubicacion_autocomplete/$',
        permission_required('auth.view_almacenes')(login_required(ubicacionAutocomplete.as_view())), 
        name='ubicacion_autocomplete'
    ),
    
    #Urls
    url(r'^nuevoproveedor/$',
    	permission_required('auth.view_almacenes')(login_required(crearProveedor.as_view())), 
    	name='nuevoproveedor'
    ),
    url(r'^listaproveedor/$',
        permission_required('auth.view_almacenes')(login_required(listaProveedor.as_view())), 
        name='listaproveedor'
    ),
    url(r'^updateproveedor/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateProveedor.as_view())), 
        name='updateproveedor'
    ),
    url(r'^nuevocliente/$',
        permission_required('auth.view_almacenes')(login_required(crearCliente.as_view())), 
        name='nuevocliente'
    ),
    url(r'^listacliente/$',
        permission_required('auth.view_almacenes')(login_required(listaCliente.as_view())), 
        name='listacliente'
    ),
    url(r'^updatecliente/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateCliente.as_view())), 
        name='updatecliente'
    ),
    url(r'^nuevotipo_entrada/$',
        permission_required('auth.view_almacenes')(login_required(crearTipoEntrada.as_view())), 
        name='nuevotipo_entrada'
    ),
    url(r'^listatipo_entrada/$',
        permission_required('auth.view_almacenes')(login_required(listaTipoEntrada.as_view())), 
        name='listatipo_entrada'
    ),
    url(r'^updatetipo_entrada/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateTipoEntrada.as_view())), 
        name='updatetipo_entrada'
    ),
    url(r'^nuevotipo_salida/$',
        permission_required('auth.view_almacenes')(login_required(crearTipoSalida.as_view())), 
        name='nuevotipo_salida'
    ),
    url(r'^listatipo_salida/$',
        permission_required('auth.view_almacenes')(login_required(listaTipoSalida.as_view())), 
        name='listatipo_salida'
    ),
    url(r'^updatetipo_salida/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateTipoSalida.as_view())), 
        name='updatetipo_salida'
    ),
    url(r'^nuevaunidad/$',
        permission_required('auth.view_almacenes')(login_required(crearUnidad.as_view())), 
        name='nuevaunidad'
    ),
    url(r'^listaunidad/$',
        permission_required('auth.view_almacenes')(login_required(listaUnidad.as_view())), 
        name='listaunidad'
    ),
    url(r'^updateunidad/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateUnidad.as_view())), 
        name='updateunidad'
    ),
    url(r'^nuevacategoria/$',
        permission_required('auth.view_almacenes')(login_required(crearCategoria.as_view())), 
        name='nuevacategoria'
    ),
    url(r'^listacategoria/$',
        permission_required('auth.view_almacenes')(login_required(listaCategoria.as_view())), 
        name='listacategoria'
    ),
    url(r'^updatecategoria/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateCategoria.as_view())), 
        name='updatecategoria'
    ),
    url(r'^nuevasubcategoria/$',
        permission_required('auth.view_almacenes')(login_required(crearSubCategoria.as_view())), 
        name='nuevasubcategoria'
    ),
    url(r'^listasubcategoria/$',
        permission_required('auth.view_almacenes')(login_required(listaSubCategoria.as_view())), 
        name='listasubcategoria'
    ),
    url(r'^updatesubcategoria/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateSubCategoria.as_view())), 
        name='updatesubcategoria'
    ),
    url(r'^nuevoitem/$',
        permission_required('auth.view_almacenes')(login_required(crearItem.as_view())), 
        name='nuevoitem'
    ),
    url(r'^listaitem/$',
        permission_required('auth.view_almacenes')(login_required(listaItem.as_view())), 
        name='listaitem'
    ),
    url(r'^listaitemt/$',
        permission_required('auth.view_almacenes')(login_required(listaItemT.as_view())), 
        name='listaitemt'
    ),
    url(r'^updateitem/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateItem.as_view())), 
        name='updateitem'
    ),
    url(r'^nuevoitemact/$',
        permission_required('auth.view_activos_f')(login_required(crearItemAct.as_view())), 
        name='nuevoitemact'
    ),
    url(r'^listaitemact/$',
        permission_required('auth.view_activos_f')(login_required(listaItemAct.as_view())), 
        name='listaitemact'
    ),
    url(r'^updateitemact/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateItemAct.as_view())), 
        name='updateitemact'
    ),
    url(r'^listaitemactivo/$',
        permission_required('auth.view_activos_f')(login_required(listaAltaAct.as_view())), 
        name='listaitemactivo'
    ),
    url(r'^nuevoingreso/$',
        #aqui el decorador de permisos
        permission_required('auth.view_almacenes')(login_required(ingresoItem.as_view())), 
        name='nuevoingreso'
    ),
    url(r'^listaingreso/$',
        #aqui el decorador de permisos
        permission_required('auth.view_almacenes')(login_required(listaIngresoItem.as_view())), 
        name='listaingreso'
    ),
    url(r'^updateingreso/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateIngresoItem.as_view())), 
        name='updateingreso'
    ),
    url(r'^nuevasalida/$',
        #aqui el decorador de permisos
        permission_required('auth.view_almacenes')(login_required(salidaItem.as_view())), 
        name='nuevasalida'
    ),
    url(r'^listasalida/$',
        #aqui el decorador de permisos
        permission_required('auth.view_almacenes')(login_required(listaSalidaItem.as_view())), 
        name='listasalida'
    ),
    url(r'^updatesalida/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(updateSalidaItem.as_view())), 
        name='updatesalida'
    ),
    url(r'^listasalidaf/$',
        permission_required('auth.view_activos_f')(login_required(listaSalidaItemf.as_view())), 
        name='listasalidaf'
    ),
    url(r'^rep_kardex_temp/$',
        permission_required('auth.view_almacenes')(login_required(reporteKardexTemplate.as_view())), 
        name='rep_kardex_temp'
    ),
    url(r'^res_kardex/$',
        permission_required('auth.view_almacenes')(login_required(resumenKardexTemplate.as_view())), 
        name='res_kardex'
    ),
    url(r'^comprobante_s/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(generarComprobanteSal.as_view())), 
        name='comprobante_s'
    ),
    url(r'^comprobante_i/(?P<pk>\d+)/$',
        permission_required('auth.view_almacenes')(login_required(generarComprobanteIng.as_view())), 
        name='comprobante_i'
    ),
    url(r'^rep_diario_e_temp/$',
        permission_required('auth.view_almacenes')(login_required(reporteDiarioETemplate.as_view())), 
        name='rep_diario_e_temp'
    ),
    url(r'^rep_diario_e/$',
        permission_required('auth.view_almacenes')(login_required(reporteDiarioE.as_view())), 
        name='rep_diario_e'
    ),
    url(r'^rep_diario_s_temp/$',
        permission_required('auth.view_almacenes')(login_required(reporteDiarioSTemplate.as_view())), 
        name='rep_diario_s_temp'
    ),
    url(r'^rep_diario_s/$',
        permission_required('auth.view_almacenes')(login_required(reporteDiarioS.as_view())), 
        name='rep_diario_s'
    ),
    url(r'^rep_kardex_v/$',
        permission_required('auth.view_almacenes')(login_required(reporteKardexVal.as_view())), 
        name='rep_kardex_v'
    ),
    url(r'^rep_resumen_kardex/$',
        permission_required('auth.view_almacenes')(login_required(resumenKardex.as_view())), 
        name='rep_resumen_kardex'
    ),
    url(r'^rep_gral/$',
        permission_required('auth.view_almacenes')(login_required(reporteGeneral.as_view())), 
        name='rep_gral'
    ),
    url(r'^resumen_eys_temp/$',
        permission_required('auth.view_almacenes')(login_required(ResumenEySTemplate.as_view())), 
        name='resumen_eys_temp'
    ),
    url(r'^reporte_resumen_eys/$',
        permission_required('auth.view_almacenes')(login_required(reporteResumenEyS.as_view())), 
        name='reporte_resumen_eys'
    ),
    url(r'^detalle_entradas/$',
        permission_required('auth.view_almacenes')(login_required(DetalleEntradasTemplate.as_view())), 
        name='detalle_entradas'
    ),
    url(r'^reporte_detalle_entradas/$',
        permission_required('auth.view_almacenes')(login_required(reporteDetalleEntradas.as_view())), 
        name='reporte_detalle_entradas'
    ),
    url(r'^detalle_salidas/$',
        permission_required('auth.view_almacenes')(login_required(DetalleSalidasTemplate.as_view())), 
        name='detalle_salidas'
    ),
    url(r'^reporte_detalle_salidas/$',
        permission_required('auth.view_almacenes')(login_required(reporteDetalleSalidas.as_view())), 
        name='reporte_detalle_salidas'
    ),
    url(r'^detalle_clientes/$',
        permission_required('auth.view_almacenes')(login_required(DetalleClientesTemplate.as_view())), 
        name='detalle_clientes'
    ),
    url(r'^reporte_detalle_clientes/$',
        permission_required('auth.view_almacenes')(login_required(reporteDetalleClientes.as_view())), 
        name='reporte_detalle_clientes'
    ),
    url(r'^detalle_proveedores/$',
        permission_required('auth.view_almacenes')(login_required(DetalleProveedoresTemplate.as_view())), 
        name='detalle_proveedores'
    ),
    url(r'^reporte_detalle_proveedores/$',
        permission_required('auth.view_almacenes')(login_required(reporteDetalleProveedores.as_view())), 
        name='reporte_detalle_proveedores'
    ),
    url(r'^act_inventario/$',
        permission_required('auth.view_almacenes')(login_required(actualizarInventario.as_view())), 
        name='act_inventario'
    ),

]










































































































"""url(r'^crearherramientas/$',
    login_required(crearHerramientas.as_view()), 
    name='crearherramientas'
),
url(r'^listaherramientas/$',
    login_required(listaHerramientas.as_view()), 
    name='listaherramientas'
),
url(r'^updateherramientas/(?P<pk>\d+)/$',
    login_required(updateHerramientas.as_view()), 
    name='updateherramientas'
),
url(r'^ingresoherramientas/(?P<ct>\w+)/$',
    login_required(ingresoHerramientasView.as_view()), 
    name='ingresoherramientas'
),
url(r'^salidaherramientas/(?P<pk>\d+)/$',
    login_required(salidaHerramientasView.as_view()), 
    name='salidaherramientas'
),
url(r'^listaitems/(?P<ct>\w+)/$',
    login_required(listaItemsPedidos.as_view()), 
    name='listaitems'
),
url(r'^crearinsumoalmacen/$',
    login_required(crearInsumoAlmacen.as_view()), 
    name='crearinsumoalmacen'
),
url(r'^updateinsumo/(?P<pk>\d+)/$',
    login_required(updateInsumo.as_view()), 
    name='updateinsumo'
),
url(r'^listainsumos/$',
    login_required(listaInsumos.as_view()), 
    name='listainsumos'
),
url(r'^ingresoinsumo/(?P<pk>\d+)/$',
    login_required(ingresoInsumoItem.as_view()), 
    name='ingresoinsumo'
),
url(r'^salidainsumo/(?P<pk>\d+)/$',
    login_required(salidaInsumoItem.as_view()), 
    name='salidainsumo'
),
url(r'^nuevomaterial/$',
    login_required(crearMaterialAlmacen.as_view()), 
    name='nuevomaterial'
),
url(r'^listamaterial/$',
    login_required(listaMaterial.as_view()), 
    name='listamaterial'
),
url(r'^materialupdate/(?P<pk>\d+)/$',
    login_required(MaterialUpdate.as_view()), 
    name='materialupdate'
),
url(r'^ingresomaterial/(?P<pk>\d+)/$',
    login_required(ingresoMaterialItem.as_view()), 
    name='ingresomaterial'
),
url(r'^salidamaterial/(?P<pk>\d+)/$',
    login_required(salidaMaterialItem.as_view()), 
    name='salidamaterial'
),
url(r'^crearmaquinariaequipo/$',
    login_required(crearMaquinariaEquipo.as_view()), 
    name='crearmaquinariaequipo'
),
url(r'^listamaquinariaequipo/$',
    login_required(listaMaquinariaEquipo.as_view()), 
    name='listamaquinariaequipo'
),
url(r'^updatemaquinariaequipo/(?P<pk>\d+)/$',
    login_required(updateMaquinariaEquipo.as_view()), 
    name='updatemaquinariaequipo'
),
url(r'^ingresomaquinariaequipo/(?P<ct>\w+)/$',
    login_required(ingresoMaquinariaEquipo.as_view()), 
    name='ingresomaquinariaequipo'
),
url(r'^salidamaquinariaequipo/(?P<pk>\d+)/$',
    login_required(salidaMaquinariaEquipo.as_view()), 
    name='salidaMaquinariaEquipo'
),
url(r'^listaingresoinsumo/(?P<pk>\d+)/$',
    login_required(listaIngresoInsumoItem.as_view()), 
    name='listaingresoinsumo'
),
url(r'^listaingresomaterial/(?P<pk>\d+)/$',
    login_required(listaIngresoMaterialItem.as_view()), 
    name='listaingresomaterial'
),
url(r'^listasalidamaterial/(?P<pk>\d+)/$',
    login_required(listaSalidaMaterial.as_view()), 
    name='listasalidamaterial'
),
url(r'^listasalidainsumo/(?P<pk>\d+)/$',
    login_required(listaSalidaInsumo.as_view()), 
    name='listasalidainsumo'
),
url(r'^listasalidaherramientas/(?P<pk>\d+)/$',
    login_required(listaSalidaHerramientas.as_view()), 
    name='listasalidaherramientas'
),
url(r'^listasalidamaquinariaequipo/(?P<pk>\d+)/$',
    login_required(listaSalidaMaquinariaEquipo.as_view()), 
    name='listasalidamaquinariaequipo'
),
url(r'^listaconfirmacionherramientas/(?P<ct>\w+)/$',
    login_required(listaConfirmacionHerramientas.as_view()), 
    name='listaconfirmacionherramientas'
),
url(r'^debolucionherramientas/(?P<pk>\d+)/$',
    login_required(debolucionHerramientas.as_view()), 
    name='debolucionherramientas'
),
url(r'^listaconfirmacionmaquinariahequipo/(?P<ct>\w+)/$',
    login_required(listaConfirmacionMaquinariaHequipo.as_view()), 
    name='listaconfirmacionmaquinariahequipo'
),
url(r'^debolucionmaquinariahequipo/(?P<pk>\d+)/$',
    login_required(debolucionMaquinariaHequipo.as_view()), 
    name='debolucionmaquinariahequipo'
),
url(r'^creartipoactivo/$',
    login_required(crearTipoActivo.as_view()), 
    name='creartipoactivo'
),

url(r'^listacrearactivo/$',
    login_required(listaCrearActivo.as_view()), 
    name='listacrearactivo'
),

url(r'^crearactivodepreciasion/(?P<pk>\d+)/$',
    login_required(crearActivoDepreciasion.as_view()), 
    name='crearactivodepreciasion'
),
url(r'^crearactivo/$',
    login_required(crearActivo.as_view()), 
    name='crearactivo'
),
url(r'^updateactivo/(?P<pk>\d+)/$',
    login_required(updateActivo.as_view()), 
    name='updateactivo'
),
url(r'^reportealmacen/(?P<ct>\w+)/$',
    login_required(reporteAlmacen.as_view()), 
    name='reportealmacen'
),
url(r'^reporteactivo/$',
    login_required(reporteActivo.as_view()), 
    name='reporteactivo'
),
url(r'^reportematerial/(?P<pk>\d+)/$',
    login_required(envio_reporte_material.as_view()), 
    name='reportematerial'
),
url(r'^envioinsumo/(?P<pk>\d+)/$',
    login_required(envio_reporte_insumo.as_view()), 
    name='envioinsumo'
),"""