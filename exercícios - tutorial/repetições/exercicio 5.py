n = int(input('Digite o valor de n: '))

a, b = 0, 1
k = 1
print(a)
print(b)
while k <= n-2:
    a, b = b, a + b
    print(b)
    k = k + 1

#print (b)

