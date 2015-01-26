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
    print ("---------- 4) Consultar cadastro de produto ----")
    print ("---------- 5) Sair  ----------------------------")
    a = int(input("Digite o número da opção: "))
    if (a == 1):
        cadastrar()
    elif (a == 2):
        editar()
    elif (a == 3):
        remover()
    elif (a == 4):
        consultar()
    elif (a == 5):
        exit()
    else:
        input("Digite uma opção válida")
        menu()
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
    print("Pesquise qual registro deseja editar")
    print(" 1) Pesquisa por nome")
    print(" 2) Pesquisa por código")
    resposta = int(input("Digite 1 ou 2 para o método de pesquisa: "))
    if (resposta == 1):
        nome_produto = raw_input("Digite o nome do produto que deseja editar: ")
	for k, v in produtos.iteritems():
	    if (v[0] == nome_produto):
		print("Registro %s %s" % (k, v))
		response = raw_input("Deseja editar esse registro [s ou n]")
		if response == "s":
		    nome = raw_input("Nome do produto: ")
		    descricao = raw_input("Descricao do produto: ")
    		    valor = input("Preço do produto: ")
		    global produtos
		    produtos = { k: [nome, descricao, valor] }
		else:
		    print("Digite um valor válido: s ou n")
		    editar()
    elif (resposta == 2):
	cod = input("Digite o código: ")
	prod = produtos.get(cod)
	print("Registro ", prod)
	nome = raw_input("Nome do produto: ")
        descricao = raw_input("Descricao do produto: ")
        valor = input("Preço do produto: ")
	global produtos
        produtos = { cod: [nome, descricao, valor] }
    else:
        input("Digite uma opção válida")
        editar()
    os.system('clear') # on linux / os x
    menu()
   
def showprodutos():
    for k, v in produtos.iteritems():
	print k, v

menu()
