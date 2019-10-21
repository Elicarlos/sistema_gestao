from django.contrib import admin
from .models import Tipo_entrada, Tipo_saida, Entrada, Saida

# Register your models here.

admin.site.register(Tipo_entrada)
admin.site.register(Tipo_saida)
admin.site.register(Entrada)
admin.site.register(Saida)