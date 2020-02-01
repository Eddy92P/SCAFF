from django import template
from contabilidad.models import *

register = template.Library()

#Balance General
@register.simple_tag
def debe_b_u(nivel_uno, f1, f2):	
	return nivel_uno.debe_b_t(f1, f2)

@register.simple_tag
def haber_b_u(nivel_uno, f1, f2):	
	return nivel_uno.haber_b_t(f1, f2)

@register.simple_tag
def debe_d_u(nivel_uno, f1, f2):	
	return nivel_uno.debe_d_t(f1, f2)
	
@register.simple_tag
def haber_d_u(nivel_uno, f1, f2):	
	return nivel_uno.haber_d_t(f1, f2)

@register.simple_tag
def saldo_b_u(nivel_uno, f1, f2):	
	return nivel_uno.saldo_b_t(f1, f2)
	
@register.simple_tag
def saldo_d_u(nivel_uno, f1, f2):	
	return nivel_uno.saldo_d_t(f1, f2)

@register.simple_tag
def debe_b_d(nivel_dos, f1, f2):	
	return nivel_dos.debe_b_t(f1, f2)

@register.simple_tag
def haber_b_d(nivel_dos, f1, f2):	
	return nivel_dos.haber_b_t(f1, f2)

@register.simple_tag
def debe_d_d(nivel_dos, f1, f2):	
	return nivel_dos.debe_d_t(f1, f2)
	
@register.simple_tag
def haber_d_d(nivel_dos, f1, f2):	
	return nivel_dos.haber_d_t(f1, f2)

@register.simple_tag
def saldo_b_d(nivel_dos, f1, f2):	
	return nivel_dos.saldo_b_t(f1, f2)
	
@register.simple_tag
def saldo_d_d(nivel_dos, f1, f2):	
	return nivel_dos.saldo_d_t(f1, f2)

@register.simple_tag
def debe_b_t(nivel_tres, f1, f2):	
	return nivel_tres.debe_b_t(f1, f2)

@register.simple_tag
def haber_b_t(nivel_tres, f1, f2):	
	return nivel_tres.haber_b_t(f1, f2)

@register.simple_tag
def debe_d_t(nivel_tres, f1, f2):	
	return nivel_tres.debe_d_t(f1, f2)
	
@register.simple_tag
def haber_d_t(nivel_tres, f1, f2):	
	return nivel_tres.haber_d_t(f1, f2)

@register.simple_tag
def saldo_b_t(nivel_tres, f1, f2):	
	return nivel_tres.saldo_b_t(f1, f2)
	
@register.simple_tag
def saldo_d_t(nivel_tres, f1, f2):	
	return nivel_tres.saldo_d_t(f1, f2)

@register.simple_tag
def debe_b_c(nivel_cuatro, f1, f2):	
	return nivel_cuatro.debe_b_t(f1, f2)

@register.simple_tag
def haber_b_c(nivel_cuatro, f1, f2):	
	return nivel_cuatro.haber_b_t(f1, f2)

@register.simple_tag
def debe_d_c(nivel_cuatro, f1, f2):	
	return nivel_cuatro.debe_d_t(f1, f2)
	
@register.simple_tag
def haber_d_c(nivel_cuatro, f1, f2):	
	return nivel_cuatro.haber_d_t(f1, f2)

@register.simple_tag
def saldo_b_c(nivel_cuatro, f1, f2):	
	return nivel_cuatro.saldo_b_t(f1, f2)
	
@register.simple_tag
def saldo_d_c(nivel_cuatro, f1, f2):	
	return nivel_cuatro.saldo_d_t(f1, f2)

@register.simple_tag
def debe_b_ci(nivel_cinco, f1, f2):	
	return nivel_cinco.debe_b_t(f1, f2)

@register.simple_tag
def haber_b_ci(nivel_cinco, f1, f2):	
	return nivel_cinco.haber_b_t(f1, f2)

@register.simple_tag
def debe_d_ci(nivel_cinco, f1, f2):	
	return nivel_cinco.debe_d_t(f1, f2)
	
@register.simple_tag
def haber_d_ci(nivel_cinco, f1, f2):	
	return nivel_cinco.haber_d_t(f1, f2)

@register.simple_tag
def saldo_b_ci(nivel_cinco, f1, f2):	
	return nivel_cinco.saldo_b_t(f1, f2)
	
@register.simple_tag
def saldo_d_ci(nivel_cinco, f1, f2):	
	return nivel_cinco.saldo_d_t(f1, f2)

@register.simple_tag
def debe_b_a(asiento, f1, f2):	
	return asiento.debe_b_t(f1, f2)

@register.simple_tag
def haber_b_a(asiento, f1, f2):	
	return asiento.haber_b_t(f1, f2)

@register.simple_tag
def debe_d_a(asiento, f1, f2):	
	return asiento.debe_d_t(f1, f2)
	
@register.simple_tag
def haber_d_a(asiento, f1, f2):	
	return asiento.haber_d_t(f1, f2)

@register.simple_tag
def saldo_b_a(asiento, f1, f2):	
	return asiento.saldo_b_t(f1, f2)
	
@register.simple_tag
def saldo_d_a(asiento, f1, f2):	
	return asiento.saldo_d_t(f1, f2)

#Estado de Resultados
@register.simple_tag
def debe_b_u_er(nivel_uno, f1, f2):	
	return nivel_uno.debe_b_ter(f1, f2)

@register.simple_tag
def haber_b_u_er(nivel_uno, f1, f2):	
	return nivel_uno.haber_b_ter(f1, f2)

@register.simple_tag
def debe_d_u_er(nivel_uno, f1, f2):	
	return nivel_uno.debe_d_ter(f1, f2)
	
@register.simple_tag
def haber_d_u_er(nivel_uno, f1, f2):	
	return nivel_uno.haber_d_ter(f1, f2)

@register.simple_tag
def saldo_b_u_er(nivel_uno, f1, f2):	
	return nivel_uno.saldo_b_ter(f1, f2)
	
@register.simple_tag
def saldo_d_u_er(nivel_uno, f1, f2):	
	return nivel_uno.saldo_d_ter(f1, f2)