#Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos
#Calcular e escrever a média aritmética dessas notas lidas
som = 0
qnt = int(input("Digite a quantidade de alunos: "))
for x in range (1,qnt+1):
    nota = float(input(f"Digite a {x} do aluno: "))
    som += nota
media = som/qnt
print(f"{media:.2f}")