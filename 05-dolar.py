import os
os.system("cls")

print("=== Seja bem vindo ao convertor de dólar ===")

dolar = float(input("Digite o valor em dólar: "))

real = dolar * 5.18
resultado = round(real, 2)

input("Precione <Enter> para ver o resultado")
os.system("cls")

print("Seu valor em dólar:",dolar)
print("Seu valor em real:",resultado)
