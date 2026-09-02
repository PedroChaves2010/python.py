import os
os.system("cls")

print("=== Programa para saber a sua idade em 2035 ===")

idade = int(input("Digite a sua idade: "))

from datetime import date

ano_nasceu = date.today().year - idade

idade_2035 = 2035 - ano_nasceu

input("Precione <Enter> para exibir a sua idade em 2035")
os.system("cls")

print(f"Essa sere a sua em 2035: {idade_2035} anos")