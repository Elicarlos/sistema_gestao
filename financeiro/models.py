from django.contrib.auth.models import User
from django.db import models




class Usuario(models.Model):
    usuario = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    
    def __str__(self):
        return str(self.usuario)
   
class Tipo_conta(models.Model):
    tipo_conta = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tipo_conta)


class Conta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    tipo_conta = models.ForeignKey(Tipo_conta, on_delete=models.PROTECT)    
    descricao_conta = models.CharField(max_length=50)
    saldo = models.FloatField(default=0)
    def __str__(self):
        return str(self.descricao_conta)

    

class Tipo_receita(models.Model):
    tipo_receita = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'tipo_receita'
    def __str__(self):
        return str(self.tipo_receita)



class Tipo_despesa(models.Model):
    tipo_despesa = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'tipo_despesa'
    def __str__(self):
        return str(self.tipo_despesa)

    
class Receita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    tipo_receita = models.ForeignKey(Tipo_receita, on_delete=models.PROTECT)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    valor = models.FloatField()
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)     
    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        

    def __str__(self):
        return str(self.descricao)

    # def total_entrada(self):
    #     total_entrada += self.valor
    #     print(total_entrada)
    #     return total_entrada   


class Despesa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    tipo_despesa = models.ForeignKey(Tipo_despesa, on_delete=models.PROTECT)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    valor = models.FloatField()
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'      
        
    def __str__(self):
        return str(self.tipo_despesa)

    # def total_saida(self):
    #     total_saida += self.tipo_despesas
    #     print(total_saida)
    #     return total_saida




    
    
  

