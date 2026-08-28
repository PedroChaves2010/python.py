import os
os.system("cls")

print("Exemplo habilitção")
idade = int(input("Informe a sua idade:"))

if idade >= 18:
    possui_carteira = input("Possui carteira de motorista?\n(1-sim ou 2-não):")

    if possui_carteira == "1":
        print("Você pode dirigir")
    elif possui_carteira == "2":
        print("Você não possui carteira de motorista")
else:
    print("Você não pode dirigir")