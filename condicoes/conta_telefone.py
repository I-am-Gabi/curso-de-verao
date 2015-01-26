minutos = int(input("Quantos minutos você utilizou este mês: "))
if minutos < 200:
    preço = 0.20
else:
    if minutos < 4000:
        preço = 0.10
    else:
        preço = 0.15
print("Você vai pagar este mês: R$ %6.2f" % (minutos * preço))
