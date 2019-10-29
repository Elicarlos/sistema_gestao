from .models import Tipo_entrada, Tipo_saida, Entrada, Saida
from rest_framework import serializers

class Tipo_entradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_entrada
        fields = ['tipo_entrada']


class  Tipo_saidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_saida
        fields = ['tipo_saida']


class EntradaSerializer(serializers.HyperlinkedModelSerializer):
    tipo_entrada = Tipo_entradaSerializer()
    class Meta:
        model = Entrada
        fields = ['valor', 'descricao', 'data', 'tipo_entrada']


class SaidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Saida
        fields = ['valor', 'descricao', 'data']



