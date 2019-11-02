from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from .models import Despesa, Tipo_despesa, Receita, Tipo_receita, Conta, Tipo_conta, Usuario
from django.db.models import Sum

from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.parsers import  JSONParser
from .serializers import TipoDespesaSerializer, TipoReceitaSerializer, ReceitaSerializer, UserSerializer
from .serializers import DespesaSerializer, UsuarioSerializer, ContaSerializer, TipoContaSerializer
from rest_framework import permissions
from financeiro.permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.usuario)


class UserDetail(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

@api_view(['GET', 'POST'])
def tipo_receita_list(request, format=None):
    if request.method == 'GET':
        tipos = Tipo_receita.objects.all()
        serializer = TipoReceitaSerializer(tipos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TipoContaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Adicionando um formatargumento de palavra
@api_view(['GET', 'PUT', 'DELETE'])
def tipo_receita_detail(request, pk, format=None):
    
    try:
        tipo = Tipo_receita.objects.get(pk=pk)
    
    except Tipo_receita.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TipoReceitaSerializer(tipo, data=request.data)


    elif request.method == 'PUT':
        serializer = TipoContaSerializer(tipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TipoReceitaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_receita.objects.all()
    serializer_class = TipoReceitaSerializer



## Views Baseadas em classes
class TipoDespesaList(APIView):
    def get(self, request, format=None):
        tipos = Tipo_despesa.objects.all()
        serializer = TipoDespesaSerializer(tipos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipoDespesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errros, status=status.HTTP_400_BAD_REQUEST)

class TipoDespesaDetail(APIView):
    def get_object(self, pk):        
        try:
            return Tipo_despesa.objects.get(pk=pk)

        except Tipo_despesa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tipo = self.get_object(pk)
        serializer = TipoDespesaSerializer(tipo)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        tipo = self.get_object(pk)
        serializer = TipoDespesaSerializer(tipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tipo = self.get_object(pk)
        tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## Usando Mixins e Generics
class TipoDespesa(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Tipo_despesa.objects.all()
    serializer_class = TipoDespesaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TipoDespesaDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Tipo_despesa.objects.all()
    serializer_class = TipoDespesaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrive(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class TipoDespesaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_despesa.objects.all()
    serializer_class = TipoDespesaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

def receitas_list(request):
    if request.method == 'GET':
        receitas = Receita.objects.all()
        serializer = ReceitaSerializer(receitas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReceitaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)

@csrf_exempt
def receitas_detail(request, pk):
    try:
        receita = Receita.objects.get(pk=pk)

    except Receita.DoesNotExists:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ReceitaSerializer(receita)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReceitaSerializer(receita, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)    

    elif request.method == 'DELETE':
        receita.delete()
        return HttpResponse(status=204)                


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

## Uso de Views Genericas
class ContaList(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class ContaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class TipoContaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_conta.objects.all()
    serializer_class = TipoContaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@csrf_exempt
def usuario_list(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe=False)







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