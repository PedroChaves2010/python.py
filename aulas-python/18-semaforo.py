import os 
os.system("cls")

semaforo = input("Informe a cor do semaforo: ")

if semaforo == "verde":
    print("Pode passar")
elif semaforo == "amarelo":
    print("Atenção!")
elif semaforo == "vermelho":
    print("Pare!!")
else:
    print("Cor inválida")