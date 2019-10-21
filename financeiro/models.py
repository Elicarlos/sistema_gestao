from django.db import models

# Create your models here.

class Tipo_entrada(models.Model):
    tipo_entrada = models.CharField(max_length=30)

    def __str__(self):
        return str(self.tipo_entrada)


class Tipo_saida(models.Model):
    tipo_saida = models.CharField(max_length=30)

    def __str__(self):
        return str(self.tipo_saida)

    
class Entrada(models.Model):
    tipo_entrada = models.ForeignKey(Tipo_entrada, on_delete=models.PROTECT)
    valor = models.FloatField()
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return str(self.tipo_entrada)


class Saida(models.Model):
    tipo_saida = models.ForeignKey(Tipo_saida, on_delete=models.PROTECT)
    valor = models.FloatField()
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return str(self.tipo_saida)
