#Escreva um código para leitura das notas de turma de 5 alunos e guarde em um vetor
#Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada
#Escrever a média da turma e o resultado da contagem
som=0
cont=0
notas= ['','','','','']
tam=len (notas)
for i in range(tam):
   notas[i]=float(input("Digite as notas: "))
for x in range (tam):
    som = notas[x] + som
media = som / tam
for y in range(tam):
    if notas[y]>=media:
       cont+=1
print(f"Temos {cont} alunos maior do que a média {media}")