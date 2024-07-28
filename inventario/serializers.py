from rest_framework import serializers
from .models import Categoria, TiendaCbba
from .validators import validar_nombre


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


