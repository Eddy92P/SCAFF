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

@register.simple_tag
def mostr_saldo_b_u_er(nivel_uno, f1, f2):	
	return nivel_uno.mostrar_saldo_b_ter(f1, f2)
	
@register.simple_tag
def mostr_saldo_d_u_er(nivel_uno, f1, f2):	
	return nivel_uno.mostrar_saldo_d_ter(f1, f2)

@register.simple_tag
def sum_patrimonio_pasivo_bs(nivel_uno, f1, f2):	
	return nivel_uno.suma_patrimonio_pasivo_bs(f1, f2)
	
@register.simple_tag
def sum_patrimonio_pasivo_dls(nivel_uno, f1, f2):	
	return nivel_uno.suma_patrimonio_pasivo_dls(f1, f2)



# Saldos correctos para balance
@register.simple_tag
def saldo_b_u_excel(nivel_uno, f1, f2):	
	return nivel_uno.saldo_b_t_excel(f1, f2)
	
@register.simple_tag
def saldo_d_u_excel(nivel_uno, f1, f2):	
	return nivel_uno.saldo_d_t_excel(f1, f2)

@register.simple_tag
def saldo_b_d_excel(nivel_dos, f1, f2):	
	return nivel_dos.saldo_b_t_excel(f1, f2)
	
@register.simple_tag
def saldo_d_d_excel(nivel_dos, f1, f2):	
	return nivel_dos.saldo_d_t_excel(f1, f2)

@register.simple_tag
def saldo_b_tr_excel(nivel_tres, f1, f2):	
	return nivel_tres.saldo_b_t_excel(f1, f2)
	
@register.simple_tag
def saldo_d_tr_excel(nivel_tres, f1, f2):	
	return nivel_tres.saldo_d_t_excel(f1, f2)

@register.simple_tag
def saldo_b_c_excel(nivel_cuatro, f1, f2):	
	return nivel_cuatro.saldo_b_t_excel(f1, f2)
	
@register.simple_tag
def saldo_d_c_excel(nivel_cuatro, f1, f2):	
	return nivel_cuatro.saldo_d_t_excel(f1, f2)

@register.simple_tag
def saldo_b_ci_excel(nivel_cinco, f1, f2):	
	return nivel_cinco.saldo_b_t_excel(f1, f2)
	
@register.simple_tag
def saldo_d_ci_excel(nivel_cinco, f1, f2):	
	return nivel_cinco.saldo_d_t_excel(f1, f2)

#Estado de Resultados saldos correctos
@register.simple_tag
def debe_b_u_excel(nivel_uno, f1, f2):	
	return nivel_uno.debe_b_t_excel(f1, f2)

@register.simple_tag
def haber_b_u_excel(nivel_uno, f1, f2):	
	return nivel_uno.haber_b_t_excel(f1, f2)

@register.simple_tag
def debe_d_u_excel(nivel_uno, f1, f2):	
	return nivel_uno.debe_d_t_excel(f1, f2)
	
@register.simple_tag
def haber_d_u_excel(nivel_uno, f1, f2):	
	return nivel_uno.haber_d_t_excel(f1, f2)

@register.simple_tag
def debe_b_d_excel(nivel_dos, f1, f2):	
	return nivel_dos.debe_b_t_excel(f1, f2)

@register.simple_tag
def haber_b_d_excel(nivel_dos, f1, f2):	
	return nivel_dos.haber_b_t_excel(f1, f2)

@register.simple_tag
def debe_d_d_excel(nivel_dos, f1, f2):	
	return nivel_dos.debe_d_t_excel(f1, f2)
	
@register.simple_tag
def haber_d_d_excel(nivel_dos, f1, f2):	
	return nivel_dos.haber_d_t_excel(f1, f2)

@register.simple_tag
def debe_b_tr_excel(nivel_tres, f1, f2):	
	return nivel_tres.debe_b_t_excel(f1, f2)

@register.simple_tag
def haber_b_tr_excel(nivel_tres, f1, f2):	
	return nivel_tres.haber_b_t_excel(f1, f2)

@register.simple_tag
def debe_d_tr_excel(nivel_tres, f1, f2):	
	return nivel_tres.debe_d_t_excel(f1, f2)
	
@register.simple_tag
def haber_d_tr_excel(nivel_tres, f1, f2):	
	return nivel_tres.haber_d_t_excel(f1, f2)

@register.simple_tag
def debe_b_c_excel(nivel_cuatro, f1, f2):	
	return nivel_cuatro.debe_b_t_excel(f1, f2)

@register.simple_tag
def haber_b_c_excel(nivel_cuatro, f1, f2):	
	return nivel_cuatro.haber_b_t_excel(f1, f2)

@register.simple_tag
def debe_d_c_excel(nivel_cuatro, f1, f2):	
	return nivel_cuatro.debe_d_t_excel(f1, f2)
	
@register.simple_tag
def haber_d_c_excel(nivel_cuatro, f1, f2):	
	return nivel_cuatro.haber_d_t_excel(f1, f2)

@register.simple_tag
def debe_b_ci_excel(nivel_cinco, f1, f2):	
	return nivel_cinco.debe_b_t_excel(f1, f2)

@register.simple_tag
def haber_b_ci_excel(nivel_cinco, f1, f2):	
	return nivel_cinco.haber_b_t_excel(f1, f2)

@register.simple_tag
def debe_d_ci_excel(nivel_cinco, f1, f2):	
	return nivel_cinco.debe_d_t_excel(f1, f2)
	
@register.simple_tag
def haber_d_ci_excel(nivel_cinco, f1, f2):	
	return nivel_cinco.haber_d_t_excel(f1, f2)


# Asiento exists
@register.simple_tag
def niv_uno_asiento_exists(nivel_uno, f1, f2):	
	return nivel_uno.asiento_exists(f1, f2)

@register.simple_tag
def niv_dos_asiento_exists(nivel_dos, f1, f2):	
	return nivel_dos.asiento_exists(f1, f2)

@register.simple_tag
def niv_tres_asiento_exists(nivel_tres, f1, f2):	
	return nivel_tres.asiento_exists(f1, f2)

@register.simple_tag
def niv_cuatro_asiento_exists(nivel_cuatro, f1, f2):	
	return nivel_cuatro.asiento_exists(f1, f2)

@register.simple_tag
def niv_cinco_asiento_exists(nivel_cinco, f1, f2):	
	return nivel_cinco.asiento_exists(f1, f2)
