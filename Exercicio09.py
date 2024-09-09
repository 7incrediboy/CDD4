comb = input("Qual o tipo de combústivel ?"
             "Use (G) para gasolina ou (E) para etanol ")
litr = float(input(f"Quantos litros de {comb} ? "))
eme = float((litr)*4.9)
gme = float((litr)*5.8)
if comb=="G" or comb=="g":
    (print(f"O valor gasto com gasolina, foi de R${gme}. "))
elif comb=="E" or comb=="e":
    (print(f"O valor gasto com etanol, foi de R${eme}. "))
else:
    print(f"O tipo de combustível é inválido!")