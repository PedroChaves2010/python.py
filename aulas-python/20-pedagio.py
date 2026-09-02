import os 
os.system("cls")

pedagio = int(input("Informe qual desses é o seu veiculo\n 1-Carro\n 2-Moto\n 3-Caminhão:"))

if pedagio == 1:
    print("Carro R$10,00")
elif pedagio == 2:
    print("Moto R$5,00")
elif pedagio == 3:
    print("Caminhão R$20,00")
else:
    print("Tipo inválido!")