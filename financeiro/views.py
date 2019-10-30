from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .models import Despeza, Tipo_despeza, Receita, Tipo_receita, Conta, Tipo_conta, Usuario
from django.db.models import Sum

from rest_framework import viewsets
from .serializers import TipoDespezaSerializer, TipoReceitaSerializer, ReceitaSerializer
from .serializers import DespezaSerializer, UsuarioSerializer, ContaSerializer, TipoContaSerializer


class TipoReceitaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_receita.objects.all().order_by('-tipo_receita')
    serializer_class = TipoReceitaSerializer


class TipoDespezaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_despeza.objects.all().order_by('-tipo_despeza')
    serializer_class = TipoDespezaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class DespezaViewSet(viewsets.ModelViewSet):
    queryset = Despeza.objects.all()
    serializer_class = DespezaSerializer


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class TipoContaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_conta.objects.all()
    serializer_class = TipoContaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# def relatorio_saida(request):
#     pass




# def entrada(request):
#     entradas = Entrada.objects.all()
#     total_entrada = Entrada.objects.aggregate(valor=Sum('valor'))
#     total_entrada = total_entrada['valor']
#     return render(request, 'entrada.html',{'total_entrada': total_entrada})

# def relatorio_entrada_familiar(request):
#     pass


# def relatorio_entrada_intervalo(request):
#     pass

# def relatorio_entrada_individual(request):
#     pass

# def relatorio_entrada_individual_intervalo(request):
#     pass



# def saida(request):
#     saidas = Saida.objects.all()
#     total_saida = Saida.objects.aggregate(valor=Sum('valor'))
#     total_saida = total_saida['valor']
#     return render(request, 'saida.html', {'total_saida': total_saida})

# def saldo_familiar(request):
#     total_entrada = Entrada.objects.aggregate(valor=Sum('valor'))
#     total_saida = Saida.objects.aggregate(valor=Sum('valor'))
#     saldo = total_entrada['valor'] - total_saida['valor']
#     return render(request, 'saldo.html', {'saldo': saldo})

# def saldo_individual(request):
#     pass