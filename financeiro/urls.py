from django.urls import include, path
from rest_framework import routers
from financeiro import views
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet)
router.register('receitas', views.ReceitaViewSet)
router.register('despesas', views.DespesaViewSet)
router.register('contas', views.ContaViewSet)
router.register('tipo-contas', views.TipoContaViewSet)
router.register('tipo-receitas', views.TipoReceitaViewSet)
router.register('tipo-despesas', views.TipoDespesaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('desp/', views.despesas_list),
    path('users1/', views.usuario_list),
    path('rec/', views.receitas_list),
    path('tipr/', views.tipo_receita_list),

    path('tipod/', views.TipoDespesaList.as_view()),
    path('tipod/<int:pk>/', views.TipoDespesaDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('rec/<int:pk>/', views.receitas_detail),
    path('despesas/<int:pk>/', views.despesas_detail),
   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
]

# urlpatterns = format_suffix_patterns(urlpatterns)