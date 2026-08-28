import os
os.system("cls")

nome = input("Digite o seu nome:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3
resultado = round(media, 2)

input("=== Precione <Enter> para saber a sua media ===")

os.system("cls")

if media >= 7:
    print("Sua media foi de:" , resultado,"Você passou de ano!!!")
elif media >=4 and media <7:
    print("Você esta de recuperação!!!")
else:
    print("Sua media foi de:", resultado ,"Você reprovou de ano!!!")