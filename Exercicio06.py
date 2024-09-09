nome = input("Digite seu nome: ")

print("Digite as notas de avaliação")

nota1 = float(input(f"Digite a primeira nota de {nome}: "))
nota2 = float(input(f"Digite a segunda nota de {nome}: "))
nota3 = float(input(f"Digite a terceira nota de {nome}: "))

media = ((nota1 + nota2 + nota3) / 3)

if media >= 7:
    print("----------------------------------")
    print(nome, ", Você foi aprovado, parabéns!")
    print("----------------------------------")
elif media >= 4:
    print("----------------------------------")
    print(nome, ", Você ficou de recuperação.")
    print("----------------------------------")
else:
    print("----------------------------------")
    print(nome, ", Você foi reprovado.")
    print("----------------------------------")