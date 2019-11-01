from django.contrib import admin
from .models import Conta, Tipo_conta, Usuario, Despesa, Tipo_despesa, Receita, Tipo_receita

# Register your models here.

admin.site.register(Conta)
admin.site.register(Tipo_conta)
admin.site.register(Usuario)
admin.site.register(Despesa)
admin.site.register(Tipo_despesa)
admin.site.register(Receita)
admin.site.register(Tipo_receita)