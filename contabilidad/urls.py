# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from contabilidad.views import *
from django.contrib.auth.views import login, logout_then_login, password_reset
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from .serializers_views import *

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^nuevoasiento/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearAsiento.as_view())), 
        name='nuevoasiento'
    ),
    url(r'^nuevoasiento/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearAsiento.as_view())), 
        name='nuevoasiento_alm'
    ),
    url(r'^nuevoasiento_s/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearAsiento1.as_view())), 
        name='nuevoasiento_alm_s'
    ),
    url(r'^nuevoasiento_act/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearAsiento2.as_view())), 
        name='nuevoasiento_act'
    ),
    url(r'^nuevoasiento_cap/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearAsiento3.as_view())), 
        name='nuevoasiento_cap'
    ),
    #url(r'^nuevoasiento1/(?P<pk>\d+)/$',
     # aqui el decorador de permisos
       # permission_required('auth.view_contabilidad')(login_required(crearAsiento1.as_view())), 
       # name='nuevoasiento1'
    #),
    #url(r'^nuevoasiento2/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
     #   permission_required('auth.view_contabilidad')(login_required(crearAsiento2.as_view())), 
     #   name='nuevoasiento2'
    #),
    url(r'^listaasiento/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(listaAsiento.as_view())), 
        name='listaasiento'
    ),
    url(r'^listaasientoanulado/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(listaAsientoAnulado.as_view())), 
        name='listaasientoanulado'
    ),
    url(r'^updateasiento/(?P<pk>\d+)/$',
        permission_required('auth.view_contabilidad')(login_required(updateAsiento.as_view())), 
        name='updateasiento'
    ),
    url(r'^nuevacuenta1/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearCuenta1.as_view())), 
        name='nuevacuenta1'
    ),
    url(r'^borrarcuenta/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(borrarCuenta.as_view())), 
        name='borrarcuenta'
    ),
    url(r'^updatecuenta1/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateCuenta1.as_view())), 
        name='updatecuenta1'
    ),
    url(r'^listacuenta1/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta1.as_view())), 
        name='listacuenta1'
    ),
    url(r'^nuevacuenta2/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearCuenta2.as_view())), 
        name='nuevacuenta2'
    ),
    url(r'^updatecuenta2/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateCuenta2.as_view())), 
        name='updatecuenta2'
    ),
    url(r'^listacuenta2/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta2.as_view())), 
        name='listacuenta2'
    ),
    url(r'^nuevacuenta3/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearCuenta3.as_view())), 
        name='nuevacuenta3'
    ),
    url(r'^updatecuenta3/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateCuenta3.as_view())), 
        name='updatecuenta3'
    ),
    url(r'^listacuenta3/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta3.as_view())), 
        name='listacuenta3'
    ),
    url(r'^nuevacuenta4/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearCuenta4.as_view())), 
        name='nuevacuenta4'
    ),
    url(r'^updatecuenta4/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateCuenta4.as_view())), 
        name='updatecuenta4'
    ),
    url(r'^listacuenta4/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta4.as_view())), 
        name='listacuenta4'
    ),
    url(r'^nuevacuenta5/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearCuenta5.as_view())), 
        name='nuevacuenta5'
    ),
    url(r'^updatecuenta5/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateCuenta5.as_view())), 
        name='updatecuenta5'
    ),
    url(r'^listacuenta5/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta5.as_view())), 
        name='listacuenta5'
    ),
    url(r'^listacuenta2t/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta2T.as_view())), 
        name='listacuenta2t'
    ),
    url(r'^listacuenta3t/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta3T.as_view())), 
        name='listacuenta3t'
    ),
    url(r'^listacuenta4t/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta4T.as_view())), 
        name='listacuenta4t'
    ),
    url(r'^listacuenta5tt/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta5TT.as_view())), 
        name='listacuenta5tt'
    ),
    url(r'^listacuenta5t/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta5T.as_view())), 
        name='listacuenta5t'
    ),
    url(r'^listalibromay/$',
        permission_required('auth.view_contabilidad')(login_required(listaLibroMayor.as_view())), 
        name='listalibromay'
    ),
    url(r'^nuevafactura/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearFactura.as_view())), 
        name='nuevafactura'
    ),
    url(r'^updatefactura/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateFactura.as_view())), 
        name='updatefactura'
    ),
    url(r'^listafactura/(?P<pk>\d+)/$',
        permission_required('auth.view_contabilidad')(login_required(listaFactura.as_view())), 
        name='listafactura'
    ),
    url(r'^nuevafactura_v/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearFacturaV.as_view())), 
        name='nuevafactura_v'
    ),
    url(r'^updatefactura_v/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateFacturaV.as_view())), 
        name='updatefactura_v'
    ),
    url(r'^listafactura_v/(?P<pk>\d+)/$',
        permission_required('auth.view_contabilidad')(login_required(listaFacturaV.as_view())), 
        name='listafactura_v'
    ),
    url(r'^nivel_uno_autocomplete/$',
        permission_required('auth.view_contabilidad')(login_required(nivel_unoAutocomplete.as_view())), 
        name='nivel_uno_autocomplete'
    ),
    url(r'^nivel_dos_autocomplete/$',
        permission_required('auth.view_contabilidad')(login_required(nivel_dosAutocomplete.as_view())), 
        name='nivel_dos_autocomplete'
    ),
    url(r'^nivel_tres_autocomplete/$',
        permission_required('auth.view_contabilidad')(login_required(nivel_tresAutocomplete.as_view())), 
        name='nivel_tres_autocomplete'
    ),
    url(r'^nivel_cuatro_autocomplete/$',
        permission_required('auth.view_contabilidad')(login_required(nivel_cuatroAutocomplete.as_view())), 
        name='nivel_cuatro_autocomplete'
    ),
    url(r'^asiento_autocomplete/$',
        permission_required('auth.view_contabilidad')(login_required(asientoAutocomplete.as_view())), 
        name='asiento_autocomplete'
    ),
    url(r'^listaasientof/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(listaAsientoForeign.as_view())), 
        name='listaasientof'
    ),
    url(r'^nuevafacturabol/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearFacturaBol.as_view())), 
        name='nuevafacturabol'
    ),
    url(r'^updatefacturabol/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateFacturaBol.as_view())), 
        name='updatefacturabol'
    ),
    url(r'^listafacturabol/(?P<pk>\d+)/$',
        permission_required('auth.view_contabilidad')(login_required(listaFacturaBol.as_view())), 
        name='listafacturabol'
    ),
    url(r'^nuevafacturaimp/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearFacturaImp.as_view())), 
        name='nuevafacturaimp'
    ),
    url(r'^updatefacturaimp/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateFacturaImp.as_view())), 
        name='updatefacturaimp'
    ),
    url(r'^listafacturaimp/(?P<pk>\d+)/$',
        permission_required('auth.view_contabilidad')(login_required(listaFacturaImp.as_view())), 
        name='listafacturaimp'
    ),
    url(r'^cotizacion_tcupload/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(uploadCotizacionTC.as_view())), 
        name='cotizacion_tcupload'
    ),
    url(r'^cotizacion_ufvupload/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(uploadCotizacionUFV.as_view())), 
        name='cotizacion_ufvupload'
    ),
    url(r'^nuevacotizacion_tc/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearCotizacion_tc.as_view())), 
        name='nuevacotizacion_tc'
    ),
    url(r'^updatecotizacion_tc/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateCotizacion_tc.as_view())), 
        name='updatecotizacion_tc'
    ),
    url(r'^listacotizacion_tc/$',
        permission_required('auth.view_contabilidad')(login_required(listaCotizacion_tc.as_view())), 
        name='listacotizacion_tc'
    ),
    url(r'^listacotizacion_m/$',
        permission_required('auth.view_contabilidad')(login_required(listaCotizacionM.as_view())), 
        name='listacotizacion_m'
    ),
    url(r'^nuevoproyecto/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearProyecto.as_view())), 
        name='nuevoproyecto'
    ),
    url(r'^updateproyecto/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateProyecto.as_view())), 
        name='updateproyecto'
    ),
    url(r'^listaproyecto/$',
        permission_required('auth.view_contabilidad')(login_required(listaProyecto.as_view())), 
        name='listaproyecto'
    ),
    url(r'^nuevabancarizacion/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(crearBancarizacion.as_view())), 
        name='nuevabancarizacion'
    ),
    url(r'^updatebancarizacion/(?P<pk>\d+)/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(updateBancarizacion.as_view())), 
        name='updatebancarizacion'
    ),
    url(r'^listabancarizacion/$',
        permission_required('auth.view_contabilidad')(login_required(listaBancarizacion.as_view())), 
        name='listabancarizacion'
    ),
    url(r'^movimiento_prov/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(listaProveedorMov.as_view())), 
        name='movimiento_prov'
    ),
    url(r'^comprobante/(?P<pk>\d+)/$',
        permission_required('auth.view_contabilidad')(login_required(generarComprobante.as_view())), 
        name='comprobante'
    ),
    url(r'^listafacturat/$',
        permission_required('auth.view_contabilidad')(login_required(listaFacturaT.as_view())), 
        name='listafacturat'
    ),
    url(r'^listafacturavt/$',
        permission_required('auth.view_contabilidad')(login_required(listaFacturaVT.as_view())), 
        name='listafacturavt'
    ),
    url(r'^cargas_excel/$',
        permission_required('auth.view_contabilidad')(login_required(FacturasExcel.as_view())), 
        name='cargas_excel'
    ),
    url(r'^facturasventas_excel/$',
        permission_required('auth.view_contabilidad')(login_required(FacturasVExcel.as_view())), 
        name='facturasventas_excel'
    ),
    url(r'^libro_mayor_p/$',
        permission_required('auth.view_contabilidad')(login_required(libroMayorP.as_view())), 
        name='libro_mayor_p'
    ),
    url(r'^listaasientoft/$',
        permission_required('auth.view_contabilidad')(login_required(listaAsientoForeignT.as_view())), 
        name='listaasientoft'
    ),
    url(r'^balance_gen/$',
        permission_required('auth.view_contabilidad')(login_required(balanceGen.as_view())), 
        name='balance_gen'
    ),
    url(r'^cuentas_balance/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta5TB.as_view())), 
        name='cuentas_balance'
    ),
    url(r'^estado_r/$',
        permission_required('auth.view_contabilidad')(login_required(estadoResultado.as_view())), 
        name='estado_r'
    ),
    url(r'^estado_resultados/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta5ER.as_view())), 
        name='estado_resultados'
    ),
    url(r'^sumas_saldos/$',
        permission_required('auth.view_contabilidad')(login_required(sumasSaldos.as_view())), 
        name='sumas_saldos'
    ),
    url(r'^suma_saldo/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta5SS.as_view())), 
        name='suma_saldo'
    ),
    url(r'^retencion/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(listaAsientoRetencion.as_view())), 
        name='retencion'
    ),
    url(r'^retencion_excel/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(RetencionExcel.as_view())), 
        name='retencion_excel'
    ),
    url(r'^cuenta/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(views.cuenta)), 
        name='cuenta'
    ),
    url(r'^listaplancuenta/$',
        permission_required('auth.view_contabilidad')(login_required(listaPlanCuenta.as_view())), 
        name='listaplancuenta'
    ),
    url(r'^estado_ev/$',
        permission_required('auth.view_contabilidad')(login_required(listaCuenta5TE.as_view())), 
        name='estado_ev'
    ),
    url(r'^evolucion_p/$',
        permission_required('auth.view_contabilidad')(login_required(estadoEvolucionP.as_view())), 
        name='evolucion_p'
    ),
    url(r'^lib_diario/$',
        permission_required('auth.view_contabilidad')(login_required(libroDiario.as_view())), 
        name='lib_diario'
    ),
    url(r'^costo_servicio/$',
        permission_required('auth.view_contabilidad')(login_required(ReporteCostoServicioTemplate.as_view())), 
        name='costo_servicio'
    ),
    url(r'^rep_costo_servicio/$',
        permission_required('auth.view_contabilidad')(login_required(ReporteCostoServicio.as_view())), 
        name='rep_costo_servicio'
    ),
    url(r'^rep_plan_cuenta/$',
        permission_required('auth.view_contabilidad')(login_required(RepPlanCuentas.as_view())), 
        name='rep_plan_cuenta'
    ),
    url(r'^nivel_unoupload/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(uploadNiveluno.as_view())), 
        name='nivel_unoupload'
    ),
    url(r'^nivel_dosupload/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(uploadNiveldos.as_view())), 
        name='nivel_dosupload'
    ),
    url(r'^nivel_tresupload/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(uploadNiveltres.as_view())), 
        name='nivel_tresupload'
    ),
    url(r'^nivel_cuatroupload/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(uploadNivelcuatro.as_view())), 
        name='nivel_cuatroupload'
    ),
    url(r'^nivel_cincoupload/$',
        #aqui el decorador de permisos
        permission_required('auth.view_contabilidad')(login_required(uploadNivelcinco.as_view())), 
        name='nivel_cincoupload'
    ),
    url(r'^nuevagestion/$',
        permission_required('auth.view_contabilidad')(login_required(crearGestion.as_view())), 
        name='nuevagestion'
    ),
    url(r'^listagestion/$',
        permission_required('auth.view_contabilidad')(login_required(listaGestion.as_view())), 
        name='listagestion'
    ),
    url(r'^cierregestion/(?P<pk>\d+)/$',
        permission_required('auth.view_contabilidad')(login_required(updateCierreGestion.as_view())), 
        name='cierregestion'
    ),
    url(r'^renum_comp/$',
        permission_required('auth.view_contabilidad')(login_required(renumerarComprobantes.as_view())), 
        name='renum_comp'
    ),
]