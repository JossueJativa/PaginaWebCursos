from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .models import *
from .serializer import *

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer