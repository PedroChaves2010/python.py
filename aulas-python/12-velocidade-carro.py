import os
os.system("cls")

limite_velocidade = int(input("Informe a velocidade do seu carro: "))

if limite_velocidade > 80:
    print("Multado")
else:
    print("Dentro do Limite de velocidade")