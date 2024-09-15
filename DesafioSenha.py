numer=0
senhax= int(input('Digite sua senha: '))

while numer<3:
    senha=int(input('Digite sua senha: '))
    if senha==senhax:
        print("senha correta")
        numer=3
    else:
        senha!= senhax
        print("senha incorreta")
        numer = numer+1