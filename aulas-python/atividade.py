import os
os.system("cls")

print('Bem Vindo ao TotalTicket')

cobrança = int(input("[1] - Realizar cobrança\n[2] - Sair do sistema: "))
os.system("cls")
if cobrança == 1:
    nome_cliente = input("Informe o seu nome: ")
    os.system("cls")
    tipo_veiculo = int(input("Escolha o tipo do seu veiculo:\n[1] - Moto: Valor da Hora -> R$ 5,00\n[2] - Carro: Valor da Hora -> R$ 8,00\n[3] - SUV: Valor da Hora -> R$ 12,00: "))
    os.system("cls")
    if tipo_veiculo == 1:
        tipo_veiculo = "Moto"
        horas = float(input("Informe quantas horas a sua moto ficou estacionada: "))
        valor_horas = 5 * horas
        if horas < 5:
           sem_taxa = valor_horas * 0
           valor_total_a = valor_horas + sem_taxa
           media_a = valor_total_a / horas
        elif horas >= 5:
            taxa_baixa = valor_horas * 0.05
            valor_total_b = valor_horas + taxa_baixa
            media_b = valor_total_b / horas
        elif horas >= 10:
            taxa_alta = valor_horas * 0.1
            valor_total_c = valor_horas + taxa_alta
            media_c = valor_total_c / horas

    elif tipo_veiculo == 2:
        tipo_veiculo = "Carro"
        horas = float(input("Informe quantas horas a seu carro ficou estacionada: "))
        valor_horas = 8 * horas
        if horas < 5:
           sem_taxa = valor_horas * 0
           valor_total_a = valor_horas + sem_taxa
           media_a = valor_total_a / horas
        elif horas >= 5:
            taxa_baixa = valor_horas * 0.05
            valor_total_b = valor_horas + taxa_baixa
            media_b = valor_total_b / horas
        elif horas >= 10:
            taxa_alta = valor_horas * 0.1
            valor_total_c = valor_horas + taxa_alta
            media_c = valor_total_c / horas
            
    elif tipo_veiculo == 3:
        tipo_veiculo = "SUV"
        horas = float(input("Informe quantas horas a seu SUV ficou estacionada: "))
        valor_horas = 12 * horas
        if horas < 5:
           sem_taxa = valor_horas * 0
           valor_total_a = valor_horas + sem_taxa
           media_a = valor_total_a / horas
        elif horas >= 5:
            taxa_baixa = valor_horas * 0.05
            valor_total_b = valor_horas + taxa_baixa
            media_b = valor_total_b / horas
        elif horas >= 10:
            taxa_alta = valor_horas * 0.1
            valor_total_c = valor_horas + taxa_alta
            media_c = valor_total_c / horas 

    print("================ ESTACIONAMENTO ================")
    print(f"Cliente:{nome_cliente}")

    print(f"Tipo do Veículo:{tipo_veiculo}")
    print(f"Horas Estacionodo:{horas}")

    print(f"Valor Base:{valor_horas}")
    if horas < 5:
        print(f"Valor Adicional: {sem_taxa}")
    elif horas >= 5:
        print(f"Valor Adicional:{taxa_baixa:.2f} ")
    elif horas >= 10:
        print(f"Valor Adicional:{taxa_alta:.2f} ")
    
    if horas < 5:
        print(f"Valor Total: {valor_total_a:.2f}")
    elif horas >= 5:
        print(f"Valor Total:{ valor_total_b:.2f} ")
    elif horas >= 10:
        print(f"Valor Total:{ valor_total_c:.2f} ")
    
    if horas < 5:
        print(f"Valor Médio por hora: {media_a:.2f}")
    elif horas >= 5:
        print(f"Valor Médio por hora:{ media_b:.2f} ")
    elif horas >= 10:
        print(f"Valor Médio por hora:{ media_c:.2f}")
    print(f"{nome_cliente}, Muito Obrigado por usar o TotalTicket!")
else:
    input("Precione o <Enter> para sair")


