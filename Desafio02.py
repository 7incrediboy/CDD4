tam=2
tentativas=3
usuarios= [""] * (tam)
senha= [""] * (tam)
pergunta=0
while pergunta!=4:
    pergunta=int(input("O que deseja fazer?\n"
                       "1. Cadastro\n"
                       "2. Login\n"
                       "3. Usuários\n"
                       "4. Sair\n"
                       "Digite aqui: "))
    match pergunta:
        case 1:
            for i in range(tam):
                existe_usuario= True
                while existe_usuario == True:
                    usuar_tentativa = input(f"Cadastre o nome do usuário {i+1}: ")
                    if usuar_tentativa not in usuarios:
                        existe_usuario = False
                        usuarios[i]=usuar_tentativa
                    else:
                        print("Usuário já cadastrado!")
                senha[i]= input(f"Cadastre a senha do usuário {i + 1}: ")
                print(f"Usuário {i+1} cadastrado!")
        case 2:
            while tentativas > 0:
                usuario_tent=input("Digite um usuário: ")
                if usuario_tent not in usuarios:
                    print("Usuário não cadastrado!")
                    break
                senha_tent=input("Digite sua senha: ")
                for x in range(tam):
                    if usuarios[x] == usuario_tent and senha[x] == senha_tent:
                        print("Login concluído com sucesso!")
                        tentativas=0
                if usuarios[x] != usuario_tent or senha[x] != senha_tent:
                    tentativas -= 1
                    print(f"Acesso Negado, tente novamente, você tem {tentativas} tentativas !")
            tentativas=3
        case 3:
            print("Os usuários cadastrados e suas senhas são:")
            for i in range(len(usuarios)):
                print(f"Usuário: {usuarios[i]} - Senha: {senha[i]}")
        case 4:
            print("Finalizando...")