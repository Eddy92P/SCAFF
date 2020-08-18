from django import template
from activos_f.models import *

register = template.Library()

@register.simple_tag
def val_ini(Alta_baja_activo, f, f1):	
	return Alta_baja_activo.val_ini(f, f1)

@register.simple_tag
def cap(Alta_baja_activo, f):	
	return Alta_baja_activo.cap(f)

@register.simple_tag
def factor(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.factor(fecha, fecha_ant)

@register.simple_tag
def valor_inicial(Alta_baja_activo, fecha_ant):	
	return Alta_baja_activo.valor_inicial(fecha_ant)

@register.simple_tag
def valor_inicial_r(Alta_baja_activo, fecha_ant):	
	return Alta_baja_activo.valor_inicial_r(fecha_ant)

@register.simple_tag
def valor_actual(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.valor_actual(fecha, fecha_ant)

@register.simple_tag
def actualizacion(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.actualizacion(fecha, fecha_ant)

@register.simple_tag
def deprec_gestion(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.deprec_gestion(fecha, fecha_ant)

@register.simple_tag
def deprec_acum_inicial(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.deprec_acum_inicial(fecha, fecha_ant)

@register.simple_tag
def deprec_acum_inicial_r(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.deprec_acum_inicial_r(fecha, fecha_ant)

@register.simple_tag
def valor_act_deprec_acum(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.valor_act_deprec_acum(fecha, fecha_ant)

@register.simple_tag
def actualiz_deprec_acum(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.actualiz_deprec_acum(fecha, fecha_ant)

@register.simple_tag
def deprec_acum(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.deprec_acum(fecha, fecha_ant)

@register.simple_tag
def saldo_activo(Alta_baja_activo, fecha, fecha_ant):	
	return Alta_baja_activo.saldo_activo(fecha, fecha_ant)

#capitalizacion
@register.simple_tag
def factor_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.factor_cap(fecha, fecha_ant)

@register.simple_tag
def valor_inicial_cap(Capitalizacion, fecha_ant):	
	return Capitalizacion.valor_inicial_cap(fecha_ant)

@register.simple_tag
def valor_inicial_cap_r(Capitalizacion, fecha_ant):	
	return Capitalizacion.valor_inicial_cap_r(fecha_ant)

@register.simple_tag
def valor_actual_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.valor_actual_cap(fecha, fecha_ant)

@register.simple_tag
def actualizacion_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.actualizacion_cap(fecha, fecha_ant)

@register.simple_tag
def deprec_gestion_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.deprec_gestion_cap(fecha, fecha_ant)

@register.simple_tag
def deprec_acum_inicial_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.deprec_acum_inicial_cap(fecha, fecha_ant)

@register.simple_tag
def deprec_acum_inicial_cap_r(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.deprec_acum_inicial_cap_r(fecha, fecha_ant)

@register.simple_tag
def valor_act_deprec_acum_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.valor_act_deprec_acum_cap(fecha, fecha_ant)

@register.simple_tag
def actualiz_deprec_acum_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.actualiz_deprec_acum_cap(fecha, fecha_ant)

@register.simple_tag
def deprec_acum_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.deprec_acum_cap(fecha, fecha_ant)

@register.simple_tag
def saldo_activo_cap(Capitalizacion, fecha, fecha_ant):	
	return Capitalizacion.saldo_activo_cap(fecha, fecha_ant)

#Sub totales
@register.simple_tag
def val_inic_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.val_inic_tot(fecha, fecha_ant, vinc)

@register.simple_tag
def valor_actual_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.valor_actual_tot(fecha, fecha_ant, vinc)

@register.simple_tag
def actualizacion_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.actualizacion_tot(fecha, fecha_ant, vinc)

@register.simple_tag
def deprec_gestion_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.deprec_gestion_tot(fecha, fecha_ant, vinc)

@register.simple_tag
def deprec_acum_inicial_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.deprec_acum_inicial_tot(fecha, fecha_ant, vinc)

@register.simple_tag
def valor_act_deprec_acum_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.valor_act_deprec_acum_tot(fecha, fecha_ant, vinc)

@register.simple_tag
def actualiz_deprec_acum_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.actualiz_deprec_acum_tot(fecha, fecha_ant, vinc)

@register.simple_tag
def deprec_acum_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.deprec_acum_tot(fecha, fecha_ant, vinc)

@register.simple_tag
def saldo_activo_tot(Alta_baja_activo, fecha, fecha_ant, vinc):	
	return Alta_baja_activo.saldo_activo_tot(fecha, fecha_ant, vinc)