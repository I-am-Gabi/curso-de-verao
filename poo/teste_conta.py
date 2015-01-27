# -*- coding: utf-8 -*-

from conta_corrente import Cliente, Banco, Conta

joao = Cliente("João da Silva", "1231-1231")
maria = Cliente("Maria Silva", "4423-2353")
conta = Conta([joao, maria], 100)
tatu = Banco("Tatu")
tatu.abre_conta(conta)
tatu.lista_contas()
