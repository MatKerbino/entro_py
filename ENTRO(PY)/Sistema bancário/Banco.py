menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''
dinheiro = 0
LIMITE_DIARIO = 3
atual_limite = 0
LIMITE_MAXIMO_SAQUE = 500
historico = []

def Depositar(valor):
    global dinheiro
    if valor <= 0:
        return print("Valor inválido")
        start()
    dinheiro = dinheiro + valor
    historico.append("Depósito de R${:.2f} em conta".format(valor))
    print('Foi depositado com sucesso!')
    start()

def Sacar(valor):
    global dinheiro
    global atual_limite
    if valor <= 0:
        return print("Valor inválido")
        start()
    if atual_limite == LIMITE_DIARIO:
        return print("Limite diário alcançado")
        start()
    if valor > dinheiro:
        return print("O valor de saque é maior que o saldo")
        start()
    dinheiro = dinheiro - valor
    historico.append("Saque de R${:.2f} em conta".format(valor))
    atual_limite += 1
    start()

def Extrato():
    print(historico)
    print("saldo atual: R${:.2f}".format(dinheiro))
    start()

def start():

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor para o depósito'))
        valor = int(valor)
        Depositar(valor)
    if opcao == 's':
        valor = float(input('Informe o valor para o saque'))
        valor = int(valor)
        Sacar(valor)
    if opcao == 'e':
        Extrato()
    if opcao == 'q':
        exit()
    start()

start()


