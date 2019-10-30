from django.contrib.auth.models import User, Group
from .models import Tipo_receita, Receita, Tipo_despeza, Despeza, Tipo_conta, Conta, Usuario
from rest_framework import serializers



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'id', 'usuario', 'cpf', 'email']

class TipoDespezaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_despeza
        fields= ['url','id', 'tipo_despeza']


class TipoContaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_conta
        fields = ['url','id', 'tipo_conta']

class ContaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:        
        model = Conta
        fields = ['url', 'id', 'usuario', 'tipo_conta', 'descricao_conta', 'saldo']

class  TipoReceitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_receita
        fields = ['url', 'id', 'tipo_receita']


class ReceitaSerializer(serializers.HyperlinkedModelSerializer):   
    class Meta:
        model = Receita
        fields = ['url','id', 'usuario', 'conta', 'tipo_receita','valor','descricao', 'data' ]


class DespezaSerializer(serializers.HyperlinkedModelSerializer):     
    class Meta:
        model = Despeza
        fields = ['url','id', 'usuario', 'conta', 'tipo_despeza','valor','descricao', 'data' ]



