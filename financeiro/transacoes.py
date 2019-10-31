# from .models import Despeza, Conta, Receita


def pagar_despeza():
    result = Conta.saldo - Despeza.valor
    return result

def receber_receita():
    result = Conta.saldo + Receita.valor
    return result
    