import os
os.system("cls")

ano = int(input("Informe o ano: "))
bissexto = 0
ano_bissexto = ano % 4

if ano_bissexto == bissexto:
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")