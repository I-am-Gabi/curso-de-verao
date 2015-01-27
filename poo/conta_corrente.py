# -*- coding: utf-8 -*-

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone                                           

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
	self.saldo = 0
	self.clientes = clientes
	self.numero = numero
	self.operacoes = []
	self.deposito(saldo)
    def resumo(self):
	print("CC Número: %s Saldo: %10.2f" % (self.numero, self.saldo))
    def saque(self, valor):
	if self.saldo >= valor:
	    self.saldo -= valor
	    self.operacoes.append(["SAQUE", valor])
    def deposito(self, valor):
	self.saldo += valor
	self.operacoes.append(["DEPOSITO", valor])
    def extrato(self):
	print("Extrato CC Nº %s \n" % self.numero)
	for o in self.operacoes:
	    print("%10s %10.2f" % (o[0], o[1]))
	print("\n Saldo: %10.2f\n" % self.saldo)

class Banco:
    def __init__(self, nome):
	self.nome = nome
	self.clientes = []
	self.contas = []
    def abre_conta(self, conta):
	self.contas.append(conta)
    def lista_contas(self):
	for c in self.contas:
	    c.resumo()


