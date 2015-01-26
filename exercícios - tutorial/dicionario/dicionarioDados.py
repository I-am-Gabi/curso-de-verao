nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
telefone = input("Digite seu telefone: ")
endereço = input("Digite seu endereço: ")

dicionario = {'nome': nome, 'idade': idade, 'telefone': telefone,\
              'endereço': endereço}

print('\n')
for i in dicionario.keys():
    print(i + ':  ' + dicionario[i])

