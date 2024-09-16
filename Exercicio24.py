#Escreva um código para ler as notas da primeira e segunda avaliações de um aluno
#Calcule e imprima a média desse aluno. Só devem ser aceitos valores válidos, durante a leitura
#0 a 10 para cada nota.
quest=1
while quest != 2:
    val1 = float(input("Digite a primeira nota: "))
    while val1 < 0 or val1 > 10:
        val1 = int(input("Primeira nota inválida, digite novamente: "))
    val2 = float(input("Digite a segunda nota: "))
    while val2 < 0 or val2 > 10:
        val2 = int(input("Segunda nota inválida, digite novamente: "))
    media = (val1+val2)/2
    print(f"A média do aluno é de {media}")
    quest = int(input("Digite 1 para repetir e 2 para parar: "))
print("Tchau!")
