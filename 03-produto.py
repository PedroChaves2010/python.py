import os
os.system("cls")

produto = input("Informe o nome do produto: ")
preco = float(input("Informe o preço do produto: "))
des = int(input("Informe a % de desconto: "))

total_desconto = (preco * des) / 100

valor_final = preco - total_desconto

print(produto)
print(valor_final)