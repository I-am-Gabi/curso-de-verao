#!/usr/bin/python
# -*- coding: utf-8 -*-

#clear the screan
import os

produtos = {}

def menu():
    print ("---------- BEM VINDO A COMÉRCIOS LTDA ----------")
    print ("---------- 1) Cadastrar produto       ----------")
    print ("---------- 2) Editar cadastro de produto -------")
    print ("---------- 3) Remover cadastro de produto ------")
    print ("---------- 4) Consultar cadastro de prodto -----")
    a = int(input("Digite o número da opção: "))
    if (a == 1):
        cadastrar()
    elif (a == 2):
        editar()
    elif (a == 3):
        remover()
    elif (a == 4):
        exit()
    else:
        input("Digite uma opção válida")
        menu()

def cadastrar():
    print()
    nome = raw_input("Nome do produto: ")
    descricao = raw_input("Descricao do produto: ")
    valor = input("Preço do produto: ")
    global produtos 
    cod = len(produtos) + 1
    produtos = { cod: [nome, descricao, valor] }
    os.system('clear') # on linux / os x
    menu()

def editar():
    print(" 1) Pesquisa por nome")
    print(" 2) Pesquisa por código")
    resposta = int(input("Digite 1 ou 2 para o método de pesquisa: "))
    if (resposta == 1):
        nome_produto = raw_input("Digite o nome do produto que deseja procurar: ")
	for k, v in produtos.iteritems():
	    if (v[0] == nome_produto):
		print (k, v)
    elif (resposta == 2):
        pass
    else:
        input("Digite uma opção válida")
        editar()
    
def showprodutos():
    for k, v in produtos.iteritems():
	print k, v

menu()
