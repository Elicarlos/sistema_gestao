from .models import Tipo_entrada, Tipo_saida, Entrada, Saida
from rest_framework import serializers

class Tipo_entradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_entrada
        fields = ['tipo_entrada']