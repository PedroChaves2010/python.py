import os
os.system("cls")

usuario = input("Informe o seu usuário: ")
senha = int(input("Informe a sua senha: "))

if usuario == "admin" and senha == 123:
    print("Acesso Liberado!")
else:
    print("Acesso Negado!")