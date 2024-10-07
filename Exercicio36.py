#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes
#Exiba a lista desses nomes
#Mostre os nomes na ordem inversa
nomes = ['']*5
tamanho = len (nomes)
for i in range(5):
    nomes[i] = input("Digite seu nome: ")
print(nomes)
for x in range (tamanho-1,-1,-1):
    print(nomes[x] , end=" ")