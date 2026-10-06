import os
import random 
import time

os.system("cls")

vida_usuario = 100
vida_computador = 100

print(""" 


██████╗░░█████╗░████████╗░█████╗░██╗░░░░░██╗░░██╗░█████╗░
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██║░░██║██╔══██╗
██████╦╝███████║░░░██║░░░███████║██║░░░░░███████║███████║
██╔══██╗██╔══██║░░░██║░░░██╔══██║██║░░░░░██╔══██║██╔══██║
██████╦╝██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║░░██║
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

██████╗░░█████╗░██╗░░██╗███████╗███╗░░░███╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░████║██╔══██╗████╗░██║
██████╔╝██║░░██║█████═╝░█████╗░░██╔████╔██║██║░░██║██╔██╗██║
██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██║╚██╔╝██║██║░░██║██║╚████║
██║░░░░░╚█████╔╝██║░╚██╗███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝""")

print("=== Escolha o seu Pokémon ===")
print("[1]- Charmander")
print("[2]- Squirtle")
print("[3]- Bulbasaur")
print("[4]- Sair")

pokemon_usuario = int(input("Escolha seu pokémon: "))

os.system("cls")
print("Aguarde o computador escolher o seu Pokémon...")
time.sleep(3)

pokemon_computador = random.randint(1,3)
while pokemon_usuario == pokemon_computador:
    pokemon_computador = random.randint(1,3)

#Exibindo o pokemon do usuario
if(pokemon_usuario == 1):
    print("Você escolheu o Charmander!")
elif(pokemon_usuario == 2):
    print('Você escolheu o Squirtle!')
elif(pokemon_usuario == 3):
    print("Você escolheu Bulbasaur!")

#Exibindo o pokemon do computador
if(pokemon_computador == 1):
    print("O Computador escolheu o Chamander!")
elif(pokemon_computador == 2):
    print("O Computador escolheu o Squirtle!")
elif(pokemon_computador == 3):
    print("O Computador escolheu o Bulbasaur!")

input("Precione <Enter> para iniciar a batalha!")

while vida_usuario > 0 or vida_computador > 0:
    os.system("cls")

    print(f"Sua Vida:{vida_usuario}")

    print(f"Vida do computador:{vida_computador}")

    print("=== Menu de Batalha ===")
    print("[1] - Atacar")
    print("[2] - Usar poção de cura")
    print("[3] - Fugir")

    op_usuario = int(input("Escolha uma opção: "))

    #verificar qual foi aescolha do usuario
    if(op_usuario == 1):
        print("Você atacou")
        vida_computador -= random.randint(10, 20)
    elif(op_usuario == 2):
        print("Você se curou")
        vida_usuario += 5
        print(f"Sua vida agora é:{vida_usuario}")
    elif(op_usuario == 3):
        print("Você escolheu fugir")
        vida_usuario
        break
    time.sleep(4)

    os.system("cls")

    print("Aguarde o computador escolher...")

    time.sleep(3)

    op_computador = random.randint(1,3)

    #verificar qual foi a opção escolhida pelo computador
    if(op_computador == 1):
        print("O Computador atacou")
        vida_usuario -= random.randint(10,20)
    elif(op_computador == 2):
        vida_computador += 5
        print("O Computador se curou")
        print(f"Vida so computador agora:{vida_computador}")
    elif(op_computador == 3):
        print("O Computador fugiu")
        vida_computador = 0
        break
    time.sleep(3)

#Verificar quem ganhou
if vida_usuario > vida_computador:
    print("Parabéns você ganhou!")
else:
    print("GAME OVER! O computador venceu!")

print("Jogo Finalizado")
