def piramide2(n):
    for i in range (1,n+1):
        for x in range (1,i+1):
            print(i,end=" ")
        print()
def piramide23(n):
    for i in range (1,n+1):
        for x in range(1,i+1):
            print(x,end=" ")
        print()
def vogais(texto):
    cont=0
    for x in texto:
        if x in "aeiouAEIOU":
            cont+=1
    print(cont)