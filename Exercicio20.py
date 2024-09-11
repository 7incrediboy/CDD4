#Usando while, leia 10 valores, calcule e esreva a média aritmética desses valores.
v=0
som=0
while v < 10:
    valor=int(input("Digite as notas: "))
    v = v+1
    som=valor+som
media = som/10
print(f"A média é {media:.2f}")