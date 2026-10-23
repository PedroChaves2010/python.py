import cv2

camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()
    if not sucesso:
        print("Erro ao acessor a câmera")
        break
    frame = cv2.flip(frame, 1)
    frame_hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    vmi = (0,  50, 50)
    vms = (10, 255, 255)

    ami = (15, 50, 50)
    ams = (35, 255, 255)

    vdi = (40, 50, 50)
    vds = (80, 255, 255)

    azi = (92, 100, 100)
    azs = (122, 255, 255)

    mvm = cv2.inRange(frame_hsv, vmi, vms)

    mam = cv2.inRange(frame_hsv, ami, ams)

    mvd = cv2.inRange(frame_hsv, vdi, vds)

    maz = cv2.inRange(frame_hsv,azi, azs)


    pvm = cv2.countNonZero(mvm)
    pam = cv2.countNonZero(mam)
    pvd = cv2.countNonZero(mvd)
    paz = cv2.countNonZero(maz)
    limite_minimo = 10000

    if pvm > limite_minimo and pvm > pam and pvm > pvd and pvm > paz:
        mensagem ="SINAL VERMELHO: PARE O CARRO"
        cor_texto = (0, 0, 255)

    elif pam > limite_minimo and  pam > pvd and pam > pvm and  pam > paz:
        mensagem = "SINAL AMARELO: ATENÇÃO, REDUZA"
        cor_texto = (0, 255, 255)

    elif pvd > limite_minimo and pvd > pam and pvd > pvm and pvd > paz:
        mensagem = "SINAL VERDE: MANTENHA A VELCIDADE"
        cor_texto = (0, 255, 0)

    elif paz > limite_minimo and paz > pam and paz > pvm and paz > pvd:
        mensagem = "PEDESTRE INDENTIFICADO: FRENAGEM DE EMERGÊNCIA"
        cor_texto = (255, 0, 0)
    else:
        mensagem = "PROCURANDO SEMAFORO..."
        cor_texto = (255, 255, 255)

    cv2.putText(frame, mensagem, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,  cor_texto, 2)

    cv2.imshow("Detecção ded semaforo", frame)
    cv2.imshow("Teste", maz)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.realease()
cv2.destroyAllWindows()
