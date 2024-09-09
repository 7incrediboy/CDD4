#Ler uma variável de número inteiro e mostrar a tabuada de multiplicação desse número (1-10).
#Formato de saída: 1x5 = 5 2x5 = 10
num = int(input("Digite um número: "))

for x in range (1,11):
    numer = num * x
    print(f"{num} x {x} = {numer}")
