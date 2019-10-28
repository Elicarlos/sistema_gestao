from django.db import models

# Create your models here.

class Tipo_entrada(models.Model):
    tipo_entrada = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Tipo_entrada'
    def __str__(self):
        return str(self.tipo_entrada)


class Tipo_saida(models.Model):
    tipo_saida = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Tipo_saida'
    def __str__(self):
        return str(self.tipo_saida)

    
class Entrada(models.Model):
    tipo_entrada = models.ForeignKey(Tipo_entrada, on_delete=models.PROTECT)
    valor = models.FloatField()
    descricao = models.TextField()
    data = models.DateField()     
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
    def __str__(self):
        return str(self.tipo_entrada)

    def total_entrada(self):
        total_entrada += self.valor
        print(total_entrada)
        return total_entrada   


class Saida(models.Model):
    tipo_saida = models.ForeignKey(Tipo_saida, on_delete=models.PROTECT)
    valor = models.FloatField()
    descricao = models.TextField()
    data = models.DateField()
    class Meta:
        verbose_name = 'Saida'
        verbose_name_plural = 'Saidas'
    def __str__(self):
        return str(self.tipo_saida)

    def total_saida(self):
        total_saida += self.tipo_saida
        print(total_saida)
        return total_saida
    
  

