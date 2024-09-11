#Faça um código que receba o número de alunos de uma sala de aula e depois solicite as notas desses alunos
#no final, mostre a média aritmética da turma
qtd= int(input("Quantos alunos tem na sala ? "))
v=0
som=0
while v < qtd:
    valor = int(input("Digite as notas: "))
    v = v + 1
    som = valor + som
media = som / qtd
print(f"A média é {media:.2f}")