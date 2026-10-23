import cv2
import os
os.system("cls")

camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    limite_inferior = (20, 100, 100)
    limite_superior = (45, 255, 255)
    mascara = cv2.inRange(hsv, limite_inferior, limite_superior)
    resultado = cv2.bitwise_and(frame, frame, mask=mascara)

    cv2.imshow("1.Imagem ORiginal (BGR)", frame)
    cv2.imshow("2.Espaço de cor (HSV)", hsv)
    cv2.imshow("3. Mascara (Rastreamento)", mascara)
    cv2.imshow("4. Resultado", resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()