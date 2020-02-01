from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *

class currentUserViewSetRest(viewsets.ModelViewSet):
	model = User
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user

	def list(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)