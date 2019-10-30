from django.contrib import admin
from .models import Conta, Tipo_conta, Usuario, Despeza, Tipo_despeza, Receita, Tipo_receita

# Register your models here.

admin.site.register(Conta)
admin.site.register(Tipo_conta)
admin.site.register(Usuario)
admin.site.register(Despeza)
admin.site.register(Tipo_despeza)
admin.site.register(Receita)
admin.site.register(Tipo_receita)