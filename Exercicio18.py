#Receber 10 números do usuário e mostre a soma de todos os números impares.
soma = 0
for x in range(10):
    numero = int(input("Digite o número: "))
    if numero %2!= 0:
        soma = soma+numero
print(soma)