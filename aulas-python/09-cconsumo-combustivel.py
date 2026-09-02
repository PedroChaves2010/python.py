import os
os.system("cls")

km = float(input("Informe quantos quilometros você percorreu:"))
litro = float(input("Informe quantos litros de combustivel foram gastos:"))

consumo = km / litro
resultado = round (consumo, 2)

os.system("cls")

input("Precione <Enter> para exibir o resultado")

print(f"Seu consumo foi de:{resultado}Km/l")