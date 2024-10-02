#Faça um código para ler 5 usuários e suas senhas, e armazenar cada lista em um array diferente
#após completar a digitação, imprimir : nome, senha e posição dos dados no array
usua = ['']*5
senha = ['']*5
tam = len (usua)
for i in range (tam):
    usua[i] = str((input("Digite o seu usuário: ")))
    senha[i] = str((input("Digite sua senha: ")))
for x in range (tam):
    print(f"usuário {x}. Login: {usua[x]} Senha: {senha[x]}.")