#ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.
opcao=0
while opcao!=2:
    x=0
    som=0
    for x in range(10):
        valor=int(input("Digite o valor: "))
        if valor < 0:
            som += 1
    print(f"Valores negativos {som}")
    opcao=int(input("Deseja continuar ?\n"
                    "1 - sim. "
                    "2 - não. "))