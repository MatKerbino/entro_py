import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    MAX_TENTATIVAS = 5

    def __init__(self, numero, identificador, cliente, senha):
        self._saldo = 0
        self._numero = numero
        self._identificador = identificador
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._senha = senha
        self._tentativas = 0
        self._bloqueada = False

    @classmethod
    def nova_conta(cls, cliente, numero, identificador, senha):
        return cls(numero, identificador, cliente, senha)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def identificador(self):
        return self._identificador

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def verificar_senha(self, senha):
        if self._bloqueada:
            print("\n@@@ Conta bloqueada! Por favor, se dirija até o banco mais próximo. @@@")
            return False

        if self._senha == senha:
            self._tentativas = 0
            return True
        else:
            self._tentativas += 1
            if self._tentativas >= Conta.MAX_TENTATIVAS:
                self._bloqueada = True
                print("\n@@@ Conta bloqueada! Por favor, se dirija até o banco mais próximo. @@@")
            else:
                print("\n@@@ Senha incorreta! Tente novamente. @@@")
            return False

    def sacar(self, valor, senha):
        if not self.verificar_senha(senha):
            return False

        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor, senha):
        if not self.verificar_senha(senha):
            return False

        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

    def transferir(self, valor, senha, conta_destino):
        if not self.verificar_senha(senha):
            return False

        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            conta_destino._saldo += valor
            print("\n=== Transferência realizada com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

class ContaCorrente(Conta):
    def __init__(self, numero, identificador, cliente, senha, limite=500, limite_saques=3):
        super().__init__(numero, identificador, cliente, senha)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor, senha):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor, senha)

        return False

    def transferir(self, valor, senha, conta_destino):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Transferencia.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor da transferência excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de transferências excedido. @@@")

        else:
            return super().transferir(valor, senha, conta_destino)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Identificador:\t{self.identificador}
            Titular:\t{self.cliente.nome}
        """

class ContaPoupanca(Conta):
    def __init__(self, numero, identificador, cliente, senha, limite=2000, limite_saques=1):
        super().__init__(numero, identificador, cliente, senha)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def saldo(self):
        rendimento = self._saldo * 0.095
        print(f"Rendimento anual estimado: R$ {rendimento:.2f}")
        return self._saldo

    def sacar(self, valor, senha):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor, senha)

        return False

    def transferir(self, valor, senha, conta_destino):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Transferencia.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor da transferência excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de transferências excedido. @@@")

        else:
            return super().transferir(valor, senha, conta_destino)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            Conta Poupança:\t{self.numero}
            Identificador:\t{self.identificador}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor, conta._senha)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor, conta._senha)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Transferencia(Transacao):
    def __init__(self, valor, conta_destino):
        self._valor = valor
        self._conta_destino = conta_destino

    @property
    def valor(self):
        return self._valor

    @property
    def conta_destino(self):
        return self._conta_destino

    def registrar(self, conta):
        sucesso = conta.transferir(self.valor, conta._senha, self._conta_destino)
        if sucesso:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Exibir Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [t] Transferir
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None

    # Vamos assumir que o cliente possui apenas uma conta para simplicidade
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("Informe o valor do depósito: "))
    senha = input("Informe a senha da conta: ")
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("Informe o valor do saque: "))
    senha = input("Informe a senha da conta: ")
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    identificador = input("Informe um identificador único de 6 dígitos: ")
    senha = input("Informe uma senha para a conta: ")
    tipo_conta = input("Informe o tipo de conta (Corrente ou Poupanca): ")

    if tipo_conta.lower() == "corrente":
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, identificador=identificador, senha=senha)
    elif tipo_conta.lower() == "poupanca":
        conta = ContaPoupanca.nova_conta(cliente=cliente, numero=numero_conta, identificador=identificador, senha=senha)
    else:
        print("\n@@@ Tipo de conta inválido! @@@")
        return

    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def transferir(clientes, contas):
    cpf = input("Informe o CPF do cliente que vai realizar a transferência: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    identificador_destino = input("Informe o identificador único da conta de destino: ")
    conta_destino = next((c for c in contas if c.identificador == identificador_destino), None)

    if not conta_destino:
        print("\n@@@ Conta de destino não encontrada! @@@")
        return

    valor = float(input("Informe o valor da transferência: "))
    senha = input("Informe a senha da conta: ")
    transacao = Transferencia(valor, conta_destino)
    cliente.realizar_transacao(conta, transacao)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "t":
            transferir(clientes, contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida! @@@")

main()
