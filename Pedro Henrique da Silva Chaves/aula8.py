import cv2
import os
os.system("cls")
imagem = cv2.imread("gt3rs.jpg")
imagem_modificada = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) 

cv2.putText(imagem, "Imagem Colorida", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,  (255, 0, 0), 2 )
cv2.putText(imagem_modificada, "Imagem Preto e Branco", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.25,  (0, 0, 0), 1 )

cv2.rectangle(imagem, (50, 25), (325, 60), (0, 255, 0), 3)

cv2.imshow("Foto", imagem)
cv2.imshow("Foto Preto e Branco", imagem_modificada)
cv2.waitKey(0)

cv2.destroyAllWindows()