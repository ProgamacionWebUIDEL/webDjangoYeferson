from rest_framework import serializers 
from .models import Libro

class LibroSerializable(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields=(
            'titulo',
            'autor'
        )