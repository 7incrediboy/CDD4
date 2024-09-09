#Ler o nome de 2 times e o número de gols marcados na partida (para cada time).
#Escrever o nome do vencedor, caso não haja vencedor deverá ser impressa a palavra EMPATE.
time1 = input("Qual o primeiro time ? ")
gol1 = int(input(f"Quantos gols o {time1} time marcou ? "))
#---
time2 = input("Qual o segundo time ? ")
gol2 = int(input(f"Quantos gols o {time2} time marcou ? "))
#---
if gol1>gol2:
    print(f"{time1}, foi o vencedor da partida.")
elif gol1==gol2:
    print("O jogo terminou empatado.")
else:
    print(f"{time2}, foi o vencedor da partida.")