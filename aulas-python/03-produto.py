import os
os.system("cls")

#Passo 01 - Entrada
print("=== Bem vindo a Calculadora de Desconto ===")

produto = input("Informe o nome do produto: ")
preco = float(input("Informe o preço do produto: "))
des = float(input("Informe a % de desconto: "))

#Passo 02 - Proscessamento
total_desconto = (preco * des) / 100

valor_final = preco - total_desconto

#Passo 03 - Saída
input("Precione <Enter> para visualizar...")
os.system("cls")

print("=== Relatório Final ===")
print("Produto:",produto)
print("Preço:",preco)
print("Desconto:",des)
print(f"Preço com desconto:{valor_final}")

input("Precione <Enter> para encerrar...")