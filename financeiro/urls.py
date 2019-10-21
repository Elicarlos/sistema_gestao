from django.urls import path
from .views import entrada, saida, saldo_familiar


urlpatterns = [
    path('entrada/', entrada, name='entrada'),
    path('saida/', saida, name='saida'),
    path('saldo/',  saldo_familiar, name='saldo_familiar'),
]