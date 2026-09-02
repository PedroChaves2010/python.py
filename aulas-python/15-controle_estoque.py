import os
os.system("cls")

print("=== Programa para controle de estoque ===")

estoque = int(input("Informe quantos produtos tem no estoque: "))

if estoque < 5:
    print("Estoque baixo!")
else:
    print("Estoque ok!")