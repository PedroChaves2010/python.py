import os 
os.system("cls")

numero = int(input("Digite um numero entra 1 e 10: "))

import random

sorteio = random.randint(1, 10)

if numero == sorteio:
    print("Arcetou!!!")
else:
    print(f"Errou! O número era:{sorteio}")