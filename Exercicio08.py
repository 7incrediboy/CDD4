#Leia os litros vendidos e o tipo de combustivel E=etanol G=gasolina, calcule e imprima o valor gasto
#Preço da GW/L = R$5,80 Preço do E/L = R$4,90
comb = input("Qual o tipo de combústivel ?"
             "Use (G) para gasolina ou (E) para etanol ")
litr = float(input(f"Quantos litros de {comb} ? "))
eme = float((litr)*4.9)
gme = float((litr)*5.8)
if comb == "E":
    (print(f"O valor gasto com etanol, foi de R${eme}. "))
else:
    (print(f"O valor gasto com gasolina, foi de R${gme}. "))