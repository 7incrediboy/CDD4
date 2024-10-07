#Faça um código para ler 10 números e guardar num array.
#Após isto, ler mais um número qualquer, calcular e escrever
#Quantas vezes ess número aparece no vetor
cont=0
num=[0]*4
tam=len(num)
for i in range (tam):
    num[i] = int(input("Digite 10 números: "))
num2=int(input("Digite um número para saber se ele foi repetido: "))
for x in range (tam):
    if num2==num[x]:
        cont+=1
print(cont)