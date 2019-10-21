"""gestao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from financeiro import urls as financeiro_urls
from financeiro.models import Entrada
from financeiro import views

from rest_framework import routers, serializers, viewsets

class EntradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrada
        fields = ['valor', 'descricao', 'data']


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer


router = routers.DefaultRouter()
router.register('entrada', EntradaViewSet)
router.register('tipo_entrada', views.Tipo_EntradaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('financeiro/', include(financeiro_urls)),
]
