
from __future__ import unicode_literals

from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    name = 'usuarios'

def create_perms():
	from django.contrib.auth.models import User
	from django.contrib.auth.models import Permission
	from django.contrib.contenttypes.models import ContentType
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_personal',
			name='Ver personal',
			content_type=content_type,
		)
	except:
		print ("permiso 1 ya aderido")
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_contabilidad',
			name='Ver contabilidad',
			content_type=content_type,
		)
	except:
		print ("permiso 2 ya aderido")
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_almacenes',
			name='Ver almacenes',
			content_type=content_type,
		)
	except:
		print ("permiso 3 ya aderido")
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_activos_f',
			name='Ver activos',
			content_type=content_type,
		)
	except:
		print ("permiso 4 ya aderido")