quest=0
while quest!=2:
    val1 = int(input("Digite o primeiro valor: "))
    val2 = int(input("Digite o segundo valor: "))
    while val2 == 0:
        val2 = int(input(f"Segundo valor inválido, digite novamente: "))
    div = val1 / val2
    quest = int(input("Digite 1 para continuar e 2 para parar: "))
print("Tchau!")