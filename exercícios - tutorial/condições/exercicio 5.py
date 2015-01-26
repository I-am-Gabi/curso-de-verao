valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite o total de meses a pagar: '))

#30% do salario
Salario30 = (salario*30)/100

#valor da prestação
prest = valor/anos

if Salario30 >= prest:
    print('---'*10)
    print("Aprovado!!! =D")
    print("Prestação máxima: %.2f" %Salario30)
    print("Sua prestação: %.2f" %prest)
else:
    print('---'*10)
    print("Não aprovado =(")
    print("Prestação máxima: %.2f" %Salario30)
    print("Sua prestação: %.2f" %prest)
