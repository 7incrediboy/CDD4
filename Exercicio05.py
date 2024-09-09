num = int(input("Digite o primeiro número :"))
num1 = int(input("Digite o segundo número :"))
if num==num1:
    print("Você digitou os números iguais.")
#Também pode ser usado o elif, que é a junção do if + else.
if num>num1:
    print(num1 , num)
else:
    print(num,num1)
