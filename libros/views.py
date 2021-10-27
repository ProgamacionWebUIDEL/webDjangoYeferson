from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LibroSerializable
from .models import Libro
# Create your views here.
class LibroVista(viewsets.ModelViewSet):
    serializer_class:LibroSerializable
    queryset=Libro.objects.all()