import cv2
objeto_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()
    frame = cv2.flip(frame, 1)
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = objeto_detector.detectMultiScale(frame_cinza, scaleFactor=1.3, minNeighbors=6)
    for (x, y, w, h) in rostos:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, "Rosto Detectado", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 1), 2)

    cv2.imshow("Aividade - IA Facial",  frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()