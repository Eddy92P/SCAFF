from django.contrib import admin
from almacenes.models import *

# Register your models here.
admin.site.register(proveedor)
admin.site.register(cliente)
admin.site.register(tipo_entrada)
admin.site.register(tipo_salida)
admin.site.register(unidad)
admin.site.register(categoria)
admin.site.register(subcategoria)                    
admin.site.register(item)
admin.site.register(itemalmacen)
admin.site.register(encingresoitem)
admin.site.register(ingresoitem)
admin.site.register(encsalidaitem)
admin.site.register(salidaitem)
