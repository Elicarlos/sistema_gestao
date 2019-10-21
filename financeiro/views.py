from django.shortcuts import render
from django.http import HttpResponse
from .models import Entrada, Saida, Tipo_entrada
from django.db.models import Sum

from rest_framework import viewsets
from .serializers import Tipo_entradaSerializer


class Tipo_EntradaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_entrada.objects.all().order_by('-tipo_entrada')
    serializer_class = Tipo_entradaSerializer

def relatorio_saida(request):
    pass




def entrada(request):
    entradas = Entrada.objects.all()
    total_entrada = Entrada.objects.aggregate(valor=Sum('valor'))
    total_entrada = total_entrada['valor']
    return render(request, 'entrada.html',{'total_entrada': total_entrada})

def relatorio_entrada_familiar(request):
    pass


def relatorio_entrada_intervalo(request):
    pass

def relatorio_entrada_individual(request):
    pass

def relatorio_entrada_individual_intervalo(request):
    pass



def saida(request):
    saidas = Saida.objects.all()
    total_saida = Saida.objects.aggregate(valor=Sum('valor'))
    total_saida = total_saida['valor']
    return render(request, 'saida.html', {'total_saida': total_saida})

def saldo_familiar(request):
    total_entrada = Entrada.objects.aggregate(valor=Sum('valor'))
    total_saida = Saida.objects.aggregate(valor=Sum('valor'))
    saldo = total_entrada['valor'] - total_saida['valor']
    return render(request, 'saldo.html', {'saldo': saldo})

def saldo_individual(request):
    pass