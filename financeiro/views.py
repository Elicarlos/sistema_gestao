from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from .models import Despesa, Tipo_despesa, Receita, Tipo_receita, Conta, Tipo_conta, Usuario
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.parsers import  JSONParser
from .serializers import TipoDespesaSerializer, TipoReceitaSerializer, ReceitaSerializer
from .serializers import DespesaSerializer, UsuarioSerializer, ContaSerializer, TipoContaSerializer


class TipoReceitaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_receita.objects.all().order_by('-tipo_receita')
    serializer_class = TipoReceitaSerializer


class TipoDespesaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_despesa.objects.all().order_by('-tipo_despesa')
    serializer_class = TipoDespesaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

@csrf_exempt
def despesas_list(request):
    # Listar todas as despesas

    if request.method == 'GET':
        despesas = Despesa.objects.all()
        serializer = DespesaSerializer(despesas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = DespesaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)



@csrf_exempt
def despesas_detail(request, pk):
    # atualiza ou deleta

    try:
        despesa = Despesa.objects.get(pk=pk)

    except Despesa.DoesNotExists:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DespesaSerializer(despesa)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = DespesaSerializer(despesa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        despesa.delete()
        return HttpResponse(serializer.data, status=404)
         

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