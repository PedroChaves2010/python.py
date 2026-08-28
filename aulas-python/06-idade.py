import os
os.system("cls")

print("=== Seja Bem-Vindo a Calculadora de Idade ===")

ano_nascimento =int(input("Digite o Ano em que você nasceu: "))
ano_atual = int(input("Digite o Ano em que estamos: "))

idade = ano_atual - ano_nascimento

input("=== Precione <Enter> para mostrar o resultado ===")
os.system("cls")

print("Sua idade é:",idade,"Anos" )