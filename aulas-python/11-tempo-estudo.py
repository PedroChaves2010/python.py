import os
os.system("cls")

tempo_estudo = float(input("Quantas horas por dia você estuda: "))

if tempo_estudo < 2:
    print("Pouco estudo")
elif tempo_estudo <=4:
    print("Estudo médio")
else:
    print("Muito estudo")