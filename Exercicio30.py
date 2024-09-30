#preencher um vetor A com 10 números. Logo em seguida, ler mais um número e guardar em X
#Armazenar em um vetor M o resultado de cada elemento de A multiplicado por x
#Imprima o vetor M
a=['','','','','','','','','','']
x=0
m=['','','','','','','','','','']
tam= len(a)
for i in range (tam):
    a[i]=int(input("Digite o número: "))
x=int(input("Digite um valor para multiplicar: "))
for y in range (tam):
    m[y]=a[y]*x
print(a)
print(x)
print(m)