#Dados os valores de horários abaixo, decifre a lógica e faça um código para executar.
#entrada01 = 3:45   entrada02 = 14:20  saída = 6:05
#recebe primeira hora
hora1= int(input("horas 1: "))
#recebe primeiro minuto
min1= int(input("minutos 1: "))
#recebe segunda hora
hora2= int(input("horas 2: "))
#recebe segundo minuto
min2= int(input("minutos 2: "))
#verifica se a primeira hora é maior que 12
if hora1 > 12:
    hora1 -= 12
#verifica se a segunda hora é maior que 12
if hora2 > 12:
    hora2 -= 12
#soma das horas
horas = hora1+hora2
#soma dos minutos
minut = min1+min2
#verifica se os minutos são maiores que 60
if minut > 60:
   minut -= 60
   horas += 1
#verifica se as horas passam de 00:00
if horas > 12:
    horas -= 12

print(f"{horas}:{minut}")