n = int(input("Digite o tamanho da agenda: "))

dic = {}
for i in range(n):
    nome = input("Digite o nome: ")
    numero = input("Digite o número: ")
    dic[nome] = numero

print('\n')
print('\tMINHA AGENDA')
print('------------------------')

for i in dic:
    print(i + ':  ' + dic[i])

print('------------------------')
