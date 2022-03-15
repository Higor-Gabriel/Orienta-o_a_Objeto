def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta,valor):
    conta["saldo"] += valor

def saque(conta,valor):
    conta["saldo"] -= valor

def extrato(conta):
    print('Saldo é {}'.format(conta['saldo']))

conta = cria_conta(123, "Higor", 55.0, 1000.0)

deposita(conta, 15.0)

saque(conta, 200)

print(extrato(conta))