import cv2
import os
os.system("cls")

camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("minha webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('n'):
        break

camera.release()
cv2.destroyAllWindows()