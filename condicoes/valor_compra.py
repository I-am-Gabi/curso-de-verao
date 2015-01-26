valor_compra = float(input("Valor da compra: "))
if valor_compra < 100:
    desconto = valor_compra * 0.10
elif valor_compra < 500:
    desconto = valor_compra * 0.20
else:
    desconto = valor_compra * 0.30
