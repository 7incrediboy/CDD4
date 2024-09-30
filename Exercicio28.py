#Criar um array tamanho 5 e preencher com os nomes dos 5 alunos, informados pelo usuário
arraynomes= ['','','','','']
tamanho=len (arraynomes)
for i in range(5):
    arraynomes[i]=input("Digite seu nome: ")
for x in range (tamanho):
    print(arraynomes[x])