#Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.
soma = 0
for numer in range(10):
    numero = int(input("Digite o número: "))
    soma = soma + numer
print(soma)