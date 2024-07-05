from abc import ABC, abstractmethod

class conta (ABC):
    pass
    

menu = '''
[c] Criar Usuário
[f] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

data = []
ifcontas = 0

def Seguranca(i):
    global data
    while True:
        senha = input('Digite a sua senha: ')
        if data[i]['tent'] == 0:
            print('Esse usuário está bloqueado. Por favor, se dirija até o banco mais próximo.')
            return False
    
        if data[i]['senha'] != senha:
            data[i]['tent'] -= 1
            print(f'Senha incorreta! Você tem apenas {data[i]["tent"]} tentativas antes da sua conta ser bloqueada!')
            if data[i]['tent'] == 0:
                print('Conta bloqueada.')
            return False
        return True

def Selecionar_conta(i, cpf):
    global data
    if not data[i]['contas']:
        print('Esse usuário não possui contas!')
        while True:
            sel = input('Deseja criar uma conta? S/N ')
            if sel.lower() == 's':
                Criar_Conta(cpf)
                break
            elif sel.lower() == 'n':
                start()
                break
            else:
                print('Opção inválida')

    for index, conta in enumerate(data[i]['contas']):
        conta_nome = list(conta.keys())[0]  
        print(f'{conta_nome} : [{index}]')

    while True:
        try:
            selecao = int(input('Selecione uma conta (número ao lado da conta): '))
            if selecao >= len(data[i]['contas']) or selecao < 0:
                print('Seleção inválida')
            else:
                return selecao
        except ValueError:
            print('Por favor, insira um número válido.')

def Criar_Usuario(nome, data_nc, cpf, endereco, senha):
    global data
    for usuario in data:
        if usuario['cpf'] == cpf:
            print('O usuário já existe no sistema!')
            return 
    proy = {'nome': nome, 'nascimento': data_nc, 'cpf': cpf, 'endereco': endereco, 'senha': senha, 'tent': 5, 'contas': []}
    data.append(proy)
    print('Usuário cadastrado com sucesso!')
    start()

def Criar_Conta(cpf):
    global data, ifcontas
    for indice, usuario in enumerate(data):
        if usuario['cpf'] == cpf:
            if Seguranca(indice) == False:
                start()
            while True:
                nome_conta = input('Digite o nome da conta: ')
                if nome_conta == '':
                    print('Nome inválido!')
                else:
                    break
            for conta in usuario['contas']:
                if nome_conta in conta:
                    print('O nome dessa conta já está cadastrado!')
                    Criar_Conta(cpf)
            
            nova_conta = {
                nome_conta: {
                    'numero da conta': ifcontas,
                    'agencia': '001',
                    'usuario': usuario['nome'],
                    'status': {'dinheiro': 0, 'atual_limite': 0, 'historico': []}
                }
            }
            
            usuario['contas'].append(nova_conta)
            ifcontas += 1
            
            print(f"Conta {nome_conta} criada com sucesso para o usuário {usuario['nome']}!")
            start()

def Depositar(cpf):
    global data
    for indice, usuario in enumerate(data):
        if usuario['cpf'] == cpf:    
            if not Seguranca(indice):
                start() 
            
            conta_index = Selecionar_conta(indice, cpf)
            conta = list(usuario["contas"][conta_index].values())[0]
             
            print(f'Valor na conta: {conta["status"]["dinheiro"]}')
            
            while True:
                valor = float(input('Informe a quantia para depositar: '))
            
                if valor < 1:
                    print('Valor inválido')
                else:
                    break
            
            conta["status"]["dinheiro"] += valor
            conta["status"]["historico"].append(f"Depósito de R${valor:.2f} em conta")
            print('O valor foi depositado com sucesso!')
            start()
    print(f'O CPF {cpf} não existe!')
    start()

def Sacar(cpf):
    global data
    for indice, usuario in enumerate(data):
        if usuario['cpf'] == cpf:    
            if not Seguranca(indice):
                start()

            conta_index = Selecionar_conta(indice, cpf)
            conta = list(usuario["contas"][conta_index].values())[0]

            if conta["status"]["atual_limite"] == 3:
                print('Limite de saque diário atingido para essa conta!')
                start()

            print(f'Valor na conta: {conta["status"]["dinheiro"]}')

            while True:
                valor = float(input('Informe a quantia para sacar (LIMITE MÁXIMO R$ 500,00): '))

                if valor < 1 or valor > 500.00:
                    print('Valor inválido para saque')
                elif valor > conta["status"]["dinheiro"]:
                    print('O valor informado é maior que a quantia na conta')
                else:
                    break

            conta["status"]["dinheiro"] -= valor
            conta["status"]["historico"].append(f"Saque de R${valor:.2f} em conta")
            conta["status"]["atual_limite"] += 1
            print('O valor foi sacado com sucesso!')
            start()

    print(f'O CPF {cpf} não existe!')
    start()

def Extrato(cpf):
    global data
    for indice, usuario in enumerate(data):
        if usuario['cpf'] == cpf:
            if not Seguranca(indice):
                start()
            conta_index = Selecionar_conta(indice, cpf)
            conta = list(usuario["contas"][conta_index].values())[0]

            print(f'{conta["status"]["historico"]} Saldo atual R${conta["status"]["dinheiro"]}')
            while True:
                c = input('Deseja ver outro extrato? S/N ')
                
                if c.lower() == 's':
                    Extrato(cpf)
                    break
                elif c.lower() == 'n':
                    print('Ok!')
                    start()
                    break
                else:
                    print('Opção inválida!')

    print(f'O CPF {cpf} não existe!')
    start()

def start():
    global data
    
    opcao = input(menu)
        
    if opcao.lower() == 'c':
        print('Ok! Vamos criar o seu usuário')
        cpf = int(input('Digite o seu cpf:  '))
        if cpf < 10000000000 or cpf > 99999999999:
            print('CPF inválido!')
            start()
        nome = input('Digite o seu nome:  ')
        data_nc = input('Digite sua data de nascimento:  ')
        endereco = input('Digite o seu endereço:  ')
        senha = input('Crie uma senha (Mínimo 4 caracteres):  ')
        if len(senha) < 4:
            senha = input('Senha inválida. Crie uma senha (Mínimo 4 caracteres):  ')
        Criar_Usuario(nome, data_nc, cpf, endereco, senha)
        
    elif opcao.lower() == 'f':
        print('Ok! Vamos criar a sua conta')
        cpf = int(input('Digite o seu cpf: '))
        if cpf < 10000000000 or cpf > 99999999999:
            print('CPF inválido!')
            start()
        Criar_Conta(cpf)
        
    elif opcao.lower() == 'd':
        cpf = int(input('Digite o seu cpf: '))
        if cpf < 10000000000 or cpf > 99999999999:
            print('CPF inválido!')
            start()
        Depositar(cpf)
        
    elif opcao.lower() == 's':
        cpf = int(input('Digite o seu cpf: '))
        if cpf < 10000000000 or cpf > 99999999999:
            print('CPF inválido!')
            start()
        Sacar(cpf)
        
    elif opcao.lower() == 'e':
        cpf = int(input('Digite o seu cpf: '))
        if cpf < 10000000000 or cpf > 99999999999:
            print('CPF inválido!')
            start()
        Extrato(cpf)
        
    elif opcao.lower() == 'q':
        exit()
        
    elif opcao.lower() == 'debug':
        print(data)
        
    else:
        print('Opção inválida!')
        start()

start()