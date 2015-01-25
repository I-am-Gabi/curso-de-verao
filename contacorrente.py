ass ContaCorrente:
    def __init__(self, conta, nome, saldo = 0):
        self.n_conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo+=valor

    def saque(self, valor):
        self.saldo-=valor

    def dados(self):
        print(self.n_conta)
        print(self.nome)
        print(self.saldo)

conta = ContaCorrente(10101, "minha")

conta.alterarNome("Maria")
conta.deposito(50)
conta.saque(1)

conta.dados()
