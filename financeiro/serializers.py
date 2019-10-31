from django.contrib.auth.models import User, Group
from .models import Tipo_receita, Receita, Tipo_despeza, Despeza, Tipo_conta, Conta, Usuario
from rest_framework import serializers



class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ['usuario', 'cpf', 'email']

class TipoDespezaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_despeza
        fields= ['tipo_despeza']


class TipoContaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_conta
        fields = ['tipo_conta']

class ContaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer().field_name="usuario"
    tipo_conta = TipoContaSerializer().field_name="tipo_conta"
    
    class Meta:        
        model = Conta
        fields = ['tipo_conta', 'usuario',  'descricao_conta', 'saldo']

class  TipoReceitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_receita
        fields = ['tipo_receita']


class ReceitaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer().field_name="usuario"
    tipo_receita = TipoReceitaSerializer().field_name="tipo_receita"
    conta = TipoContaSerializer().field_name="tipo_conta"

    class Meta:
        model = Receita
        fields = ['conta', 'usuario', 'tipo_receita','valor','descricao', 'data' ]


class DespezaSerializer(serializers.HyperlinkedModelSerializer):  
    usuario = UsuarioSerializer().field_name="usuario"
    tipo_despeza = TipoDespezaSerializer().field_name="tipo_despeza"
    conta = TipoContaSerializer().field_name="conta"

    class Meta:
        model = Despeza
        fields = ['conta', 'usuario', 'tipo_despeza','valor','descricao', 'data' ]



