import cv2

img2 = cv2.imread('Recursos\BOTW.jpg', cv2.IMREAD_COLOR)

escala = 0.7
ancho = int(img2.shape[1] * escala)
alto = int(img2.shape[0] * escala)
img2 = cv2.resize(img2, (ancho, alto), interpolation=cv2.INTER_AREA)

retval = cv2.selectROI("Imagen", img2)

img2 = img2[int(retval[1]):int(retval[1]+retval[3]), int(retval[0]):int(retval[0]+retval[2])]

mostrar = True
while mostrar:
    cv2.imshow("Ejercicio 4.2", img2)
    keypress = cv2.waitKey(1)
    if keypress == 27:
        mostrar = False
cv2.destroyAllWindows()