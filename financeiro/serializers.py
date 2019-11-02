from django.contrib.auth.models import User, Group
from .models import Tipo_receita, Receita, Tipo_despesa, Despesa, Tipo_conta, Conta, Usuario
from rest_framework import serializers




#  É SÓ DESCOMENTAR PARA FUNCIONAR 1 DESBLOQUEIO

# class UsuarioSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     usuario = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     cpf = serializers.CharField(required=True, allow_blank=True, max_length=15)
#     email = serializers.EmailField(required=True)

#     def create(self, validate_data):
#         #Cria e retorna um novo usuario
#         return Usuario.objects.create(**validate_data)

#     def update(self, instance, validate_data):
#         # Atualiza e retorna um Usuario Existente
#         instance.usuario = validate_data.get('usuario', instance.usuario)
#         instance.cpf = validate_data.get('cpf', instance.cpf)
#         instance.email = validate_data.get('email', instance.email)
#         instance.save()
#         return instance


class UserSerializer(serializers.ModelSerializer):
    usuarios = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.all())

    class Meta:
        model = Usuario
        fields = ['id', 'usuario', 'usuarios']


class UsuarioSerializer(serializers.ModelSerializer):  
    # usuarios = serializers.HyperlinkedRelatedField(
    #     many=True, view_name='users-detail', read_only=True)
  
   
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='usuario-highlight', format='html')
    class Meta:
        model = Usuario
        fields = ['id', 'usuario', 'cpf', 'email']

class TipoDespesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_despesa
        fields= ['id', 'tipo_despesa']


class TipoContaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_conta
        fields = ['id', 'tipo_conta']

class ContaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.usuario')    
    tipo_conta = TipoContaSerializer("many=False")    
    class Meta:        
        model = Conta
        fields = ['id','tipo_conta','owner', 'descricao_conta', 'saldo']

class  TipoReceitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_receita
        fields = ['id', 'tipo_receita']


class ReceitaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer("many=False")
    tipo_receita = TipoReceitaSerializer("many=False")
    conta = TipoContaSerializer("many=False")

    class Meta:
        model = Receita
        fields = ['conta', 'usuario', 'tipo_receita','valor','descricao', 'data' ]


class DespesaSerializer(serializers.HyperlinkedModelSerializer):  
    usuario = UsuarioSerializer("many=False")
    # tipo_despesa = TipoDespesaSerializer("many=False")
    # conta = TipoContaSerializer("many=False")

    class Meta:
        model = Despesa
        fields = ['id', 'usuario', 'valor','descricao', 'data' ]



