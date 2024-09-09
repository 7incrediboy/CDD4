#Receber um número do usuário e mostrar todos os números ímpares do intervalo de 1 até o número digitado
numero = int(input("Digite um número: "))

for x in range (1,numero+1,2):
    print(x)