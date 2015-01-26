# -*- coding: utf-8 -*-

pratos = 5
pilha = list(range(1, pratos+ 1))
while True:
    print("\n Existem %d pratos na pilha" % len(pilha))
    print("Pilha Atual:", pilha)
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar, S para sair.")
    operacao = raw_input("Operação (E, D ou S): ")
    if operacao == "D":
	if (len(pilha)) > 0:
	    lavado = pilha.pop(-1)
	    print("Prato %d lavado" %lavado)
	else:
	    print("Pilhar vazia! Nada para lavar")
    elif operacao == "E":
	pratos += 1 #n novo prato
	pilha.append(pratos)
    elif operacao == "S":
        break
    else:
	print("Operação inválida! Digite apenar E, D ou S")
