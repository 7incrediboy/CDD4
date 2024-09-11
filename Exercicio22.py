#Faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor
#Caso o segundo valor seja 0, solicite novamente o valor, informando que só aceita valores diferente de zero
val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
while val2 == 0:
    val2 = int(input(f"Segundo valor inválido, digite novamente: "))
div = val1/val2
print(f"O valor é {div:.2f}")
quest=int(input("Digite 1 para continuar e 2 para parar: "))
while quest == 1:
    val1 = int(input("Digite o primeiro valor: "))
    val2 = int(input("Digite o segundo valor: "))
    while val2 == 0:
        val2 = int(input(f"Segundo valor inválido, digite novamente: "))
    div = val1 / val2
print("Tchau!")