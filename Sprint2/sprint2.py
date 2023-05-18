import datetime
import getpass
hora = datetime.datetime.now().time()

if hora.hour < 12: 
    msg = "Bom dia!"
elif hora.hour < 18: 
    msg = "Boa tarde!"
else:
    msg = "Boa noite!" 

adm="administrador12"
admpass="adm123"
opc=input(f"{msg} Voce deseja logar como?\n1. Administrador\n2. Cliente\n3. Sair\n")
if opc == "1":
        while True:
            adm_input= None
            while adm_input is None:
                adm_input = input("Digite seu nome de usuário: ")
                if adm_input == "":
                    print("Usuario não encontrado, por favor digite um usuario existente ")
                    adm_input=None
                    
                if adm_input == adm:
                    adm_passinput = input("Digite sua senha: ")
                    if adm_passinput == admpass:
                        print("\n*****Login efetuado com sucesso!******\n")

                        esc=input("Digite a região que você gostaria de verificar:\n1. Zona Norte\n2. Zona Oeste\n3. Zona Sul\n4. Zona Leste\n ")
                        
                    else:
                        print("Senha incorreta!")
                    break
                break
            break
elif opc=="2":
########### PARTE DO CLIENTE
    print("oie")

elif opc=="3":
    print(f"{msg}, muito obrigado!")