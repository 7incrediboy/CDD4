#Receba um número de 1 a 12 e mostre o nome do mês correspondente
#Caso o mês não exista, mostrar "valor invalido" obs: usando If/elif/else

numes = (int(input("Digite o número do mês :")))

if numes > 12 or numes < 1:
    (print("Valor inválido"))

if numes==1:
    (print("Janeiro"))
elif numes==2:
    (print("Fevereiro"))
elif numes==3:
    (print("Março"))
elif numes==4:
    (print("Abril"))
elif numes==5:
    (print("Maio"))
elif numes==6:
    (print("Junho"))
elif numes==7:
    (print("Julho"))
elif numes==8:
    (print("Agosto"))
elif numes==9:
    (print("Setembro"))
elif numes==10:
    (print("Outubro"))
elif numes==11:
    (print("Novembro"))
elif numes==12:
    (print("Dezembro"))