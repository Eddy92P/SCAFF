from django import template
from almacenes.models import *

register = template.Library()

@register.simple_tag
def cant(fecha):	
	return item.cant(fecha)

@register.simple_tag
def tot_cant_a(item, f1):	
	return item.total_cant_a(f1)

@register.simple_tag
def tot_subt_a(item, f1):	
	return item.total_subt_a(f1)

@register.simple_tag
def alm_a_t(item, f1):
	return item.almacen_a_t(f1)

@register.simple_tag
def cat_a_t(item, f1):
	return item.categoria_a_t(f1)

@register.simple_tag
def subc_a_t(item, f1):
	return item.subcategoria_a_t(f1)

@register.simple_tag
def alm_t(item, f1, f2):
	return item.almacen_t(f1, f2)

@register.simple_tag
def cat_t(item, f1, f2):
	return item.categoria_t(f1, f2)

@register.simple_tag
def subc_t(item, f1, f2):
	return item.subcategoria_t(f1, f2)

#Saldos almacenes, categorias, subcategorias de sus respectivos modelos
@register.simple_tag
def alm_a_t(almacen, f1):
	return almacen.almacen_a_t(f1)

@register.simple_tag
def alm_a_t(almacen, f1):
	return almacen.almacen_a_t(f1)

@register.simple_tag
def cat_a_t(categoria, f1):
	return categoria.categoria_a_t(f1)

@register.simple_tag
def subc_a_t(subcategoria, f1):
	return subcategoria.subcategoria_a_t(f1)

@register.simple_tag
def alm_t(almacen, f1, f2):
	return almacen.almacen_t(f1, f2)

@register.simple_tag
def cat_t(categoria, f1, f2):
	return categoria.categoria_t(f1, f2)

@register.simple_tag
def subc_t(subcategoria, f1, f2):
	return subcategoria.subcategoria_t(f1, f2)

@register.simple_tag
def tot_sub_e(subcategoria, f1, f2):	
	return subcategoria.total_sub_e(f1, f2)

@register.simple_tag
def tot_categ_e(categoria, f1, f2):	
	return categoria.total_categ_e(f1, f2)

@register.simple_tag
def tot_alm_e(almacen, f1, f2):	
	return almacen.total_alm_e(f1, f2)

@register.simple_tag
def tot_sub_s(subcategoria, f1, f2):	
	return subcategoria.total_sub_s(f1, f2)

@register.simple_tag
def tot_categ_s(categoria, f1, f2):	
	return categoria.total_categ_s(f1, f2)

@register.simple_tag
def tot_alm_s(almacen, f1, f2):	
	return almacen.total_alm_s(f1, f2)

@register.simple_tag
def tot_cant(item, f1, f2):	
	return item.total_cant(f1, f2)

@register.simple_tag
def tot_subt(item, f1, f2):	
	return item.total_subt(f1, f2)

@register.simple_tag
def tot_cant_e(almacen, f1, f2):	
	return almacen.total_cant_e(f1, f2)

@register.simple_tag
def tot_cant_s(almacen, f1, f2):	
	return almacen.total_cant_s(f1, f2)

@register.simple_tag
def tot_cant_e(categoria, f1, f2):	
	return categoria.total_cant_e(f1, f2)

@register.simple_tag
def tot_cant_s(categoria, f1, f2):	
	return categoria.total_cant_s(f1, f2)

@register.simple_tag
def tot_cant_e(subcategoria, f1, f2):	
	return subcategoria.total_cant_e(f1, f2)

@register.simple_tag
def tot_cant_s(subcategoria, f1, f2):	
	return subcategoria.total_cant_s(f1, f2)

@register.simple_tag
def item_cant_e(item, f1, f2):	
	return item.total_cant_e(f1, f2)

@register.simple_tag
def item_cant_s(item, f1, f2):	
	return item.total_cant_s(f1, f2)

@register.simple_tag
def item_costo_u_s(item, f1, f2):	
	return item.total_costo_u_s(f1, f2)

@register.simple_tag
def tot_subt_e(item, f1, f2):	
	return item.total_subt_e(f1, f2)

@register.simple_tag
def tot_subt_s(item, f1, f2):	
	return item.total_subt_s(f1, f2)

@register.simple_tag
def tot_sub_e(item, f1, f2):	
	return item.total_sub_e(f1, f2)

@register.simple_tag
def tot_categ_e(item, f1, f2):	
	return item.total_categ_e(f1, f2)

@register.simple_tag
def tot_alm_e(item, f1, f2):	
	return item.total_alm_e(f1, f2)

@register.simple_tag
def tot_sub_s(item, f1, f2):	
	return item.total_sub_s(f1, f2)

@register.simple_tag
def tot_categ_s(item, f1, f2):	
	return item.total_categ_s(f1, f2)

@register.simple_tag
def tot_alm_s(item, f1, f2):	
	return item.total_alm_s(f1, f2)

@register.simple_tag
def subt_t_a(item, f1):	
	return item.subtotal_t_a(f1)

@register.simple_tag
def ing_t(item, f1, f2):	
	return item.ingreso_t(f1, f2)

@register.simple_tag
def sal_t(item, f1, f2):	
	return item.salida_t(f1, f2)

@register.simple_tag
def sald_t(item, f1, f2):	
	return item.saldo_t(f1, f2)

@register.simple_tag
def subtc_t_a(item, f1, c):	
	return item.subtotalcat_t_a(f1, c)

@register.simple_tag
def ingc_t(item, f1, f2, c):	
	return item.ingresocat_t(f1, f2, c)

@register.simple_tag
def salc_t(item, f1, f2, c):	
	return item.salidacat_t(f1, f2, c)

@register.simple_tag
def saldc_t(item, f1, f2, c):	
	return item.saldocat_t(f1, f2, c)

#importes para detalle de entradas y salidas
@register.simple_tag
def imp_enc(encsalidaitem, f1, f2):	
	return encsalidaitem.importe(f1, f2)

@register.simple_tag
def imp_t_s(almacen, f1, f2):	
	return almacen.importe_total_s(f1, f2)

@register.simple_tag
def imp_t(almacen, f1, f2):	
	return almacen.importe_total(f1, f2)

@register.simple_tag
def imp_t_iva(almacen, f1, f2):	
	return almacen.importe_total_iva(f1, f2)

@register.simple_tag
def imp_iva(almacen, f1, f2):	
	return almacen.importe_iva(f1, f2)

@register.simple_tag
def imp_t_s(categoria, f1, f2):	
	return categoria.importe_total_s(f1, f2)

@register.simple_tag
def imp_t(categoria, f1, f2):	
	return categoria.importe_total(f1, f2)

@register.simple_tag
def imp_t_iva(categoria, f1, f2):	
	return categoria.importe_total_iva(f1, f2)

@register.simple_tag
def imp_iva(categoria, f1, f2):	
	return categoria.importe_iva(f1, f2)

@register.simple_tag
def imp_t_s(subcategoria, f1, f2):	
	return subcategoria.importe_total_s(f1, f2)

@register.simple_tag
def imp_t(subcategoria, f1, f2):	
	return subcategoria.importe_total(f1, f2)

@register.simple_tag
def imp_t_iva(subcategoria, f1, f2):	
	return subcategoria.importe_total_iva(f1, f2)

@register.simple_tag
def imp_iva(subcategoria, f1, f2):	
	return subcategoria.importe_iva(f1, f2)

@register.simple_tag
def imp_t_s(item, f1, f2):	
	return item.importe_total_s(f1, f2)

@register.simple_tag
def imp_t_e(item, f1, f2):	
	return item.importe_total_e(f1, f2)

@register.simple_tag
def imp_t_iva(item, f1, f2):	
	return item.importe_total_iva(f1, f2)

@register.simple_tag
def imp_iva(item, f1, f2):	
	return item.importe_iva(f1, f2)

@register.simple_tag
def imp(ingresoitem, f1, f2):	
	return ingresoitem.tipo_ent_importe(f1, f2)

@register.simple_tag
def costo_t(ingresoitem, f1, f2):	
	return ingresoitem.tipo_ent_costo(f1, f2)

@register.simple_tag
def import_iva(ingresoitem, f1, f2):	
	return ingresoitem.tipo_ent_iva(f1, f2)

@register.simple_tag
def imp_s(salidaitem, f1, f2):	
	return salidaitem.tipo_sal_importe(f1, f2)

#Reporte detalle salidas por Cliente
@register.simple_tag
def cant_c_s(salidaitem, f1, f2):	
	return salidaitem.cantidad_cliente_s(f1, f2)

@register.simple_tag
def costo_u_c_s(salidaitem, f1, f2):	
	return salidaitem.costo_unit_cliente_s(f1, f2)

@register.simple_tag
def imp_c_s(salidaitem, f1, f2):
	return salidaitem.importe_cliente_s(f1, f2)

#Reporte detalle entradas por Proveedor
@register.simple_tag
def cant_p_e(ingresoitem, f1, f2):	
	return ingresoitem.cantidad_proveedor_e(f1, f2)

@register.simple_tag
def costo_u_p_e(ingresoitem, f1, f2):	
	return ingresoitem.costo_unit_proveedor_e(f1, f2)

@register.simple_tag
def imp_p_e(ingresoitem, f1, f2):
	return ingresoitem.importe_proveedor_e(f1, f2)

@register.simple_tag
def total_cat_ing(ingresoitem, f1, f2):
	return ingresoitem.total1(f1, f2)

@register.simple_tag
def total_subcat_ing(ingresoitem, f1, f2):
	return ingresoitem.total(f1, f2)

@register.simple_tag
def total_cat_sal(salidaitem, f1, f2):
	return salidaitem.total1(f1, f2)

@register.simple_tag
def total_subcat_sal(salidaitem, f1, f2):
	return salidaitem.total(f1, f2)

