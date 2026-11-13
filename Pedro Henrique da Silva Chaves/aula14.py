import cv2
import cvzone

detector_rostos = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imagem_oculos = cv2.imread('oculos_marrom.png', cv2.IMREAD_UNCHANGED)
camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()
    if not sucesso:
        break

    frame = cv2.flip(frame, 1)
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rostos = detector_rostos.detectMultiScale(frame_cinza)

    for (x, y, w, h) in rostos:
        altura_oculos = int(h / 3)
        adereco = cv2.resize(imagem_oculos, (w, altura_oculos))

        y_alvo = y + int(h / 4)
        frame = cvzone.overlayPNG(frame, adereco, [x, y_alvo])

    cv2.imshow("Filtro de óculos",  frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()