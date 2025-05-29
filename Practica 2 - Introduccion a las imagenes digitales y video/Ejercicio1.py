#Ejercicio 1

import cv2

img = cv2.imread("C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 2 - Introduccion a las imagenes digitales y video/Recursos/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 2 - Introduccion a las imagenes digitales y video/Recursos/New_Zealand_Lake.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Ventana 2.1.1", img)
cv2.waitKey(8000)
cv2.destroyAllWindows()

cv2.imshow("Ventana 2.1.2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

mostrar = True
while mostrar:
    cv2.imshow("Ventana 2.1.3", img)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        mostrar = False
cv2.destroyAllWindows()

cv2.imshow("Ventana 2.1.1", img2)
cv2.waitKey(8000)
cv2.destroyAllWindows()

cv2.imshow("Ventana 2.1.2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

mostrar = True
while mostrar:
    cv2.imshow("Ventana 2.1.3", img2)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        mostrar = False
cv2.destroyAllWindows()