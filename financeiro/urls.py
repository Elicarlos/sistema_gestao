from django.urls import include, path
from rest_framework import routers
from financeiro import views
from django.contrib import admin
from django.contrib.auth.models import User

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet)
router.register('receitas', views.ReceitaViewSet)
router.register('despezas', views.DespezaViewSet)
router.register('contas', views.ContaViewSet)
router.register('tipo-contas', views.TipoContaViewSet)
router.register('tipo-receitas', views.TipoReceitaViewSet)
router.register('tipo-despezas', views.TipoDespezaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
]