# -*- coding: utf-8 -*-

notas = [6, 7, 8, 9]
soma = 0
x = 0
while x < 5:
    # print x
    soma += notas[x]
    x += 1
print("Média: %5.2f" % (soma/x))
