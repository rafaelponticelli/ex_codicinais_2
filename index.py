import getpass   


loop = 0
while (loop < 1):
    usuario  = str(input("Digite o Nome de Usuário :")).upper

    senha = getpass.getpass('Digite sua Senha: ' ) 

    
    if (usuario == senha ):
            print("ERRO 504!")
            print("O Nome De Usuario Não Pode Ser Igual A Senha")

    if (usuario != senha):
        print("Login com Sucesso !!")