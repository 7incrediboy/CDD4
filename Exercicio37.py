#Faça um algoritmo pra ler 10 valores inteiros e armazenes em um vetor
#1-Todos os números pares que existem no vetor
#2-O menor e o maior valor existente no vetor
#3-Quantos são maiores que a média desses valores
som=0
cont2=0
num=['']*4
maior=0
menor=10
tam= len(num)
for x in range(tam):
    num[x]=int(input(f"Digite o {x + 1}º número: "))
#mostra os números pares / pode ser usado com python -> maior = max(numeros) - menor = min(numeros)
for i in range (tam):
    som = num[i] + som
    if num[i] %2==0:
        print(f"Os números pares são {num[i]}", end='')
        print()
    elif num[i]>maior:
        maior= num[i]
    if num[i]<menor:
        menor= num[i]
print(f"O maior número é {maior} e o menor é {menor}")
#mostra a média e quantos são maiores que ela
media = som / tam
for y in range(tam):
        cont2+=1
print(f"Temos {cont2} números maiores do que a média {media}")