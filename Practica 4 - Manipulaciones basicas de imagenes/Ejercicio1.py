import cv2

img1 = cv2.imread('Recursos\Hollow Knight.jpg', cv2.IMREAD_COLOR)

alto, ancho = img1.shape[:2]

tx, ty = ancho/2, alto/2

centro = (ancho/2, alto/2)
rot_matriz = cv2.getRotationMatrix2D(centro, 45, 1.0)

rot_img1 = cv2.warpAffine(img1, rot_matriz, (ancho, alto))

nuevo_ancho = 560
nuevo_alto = 540
nuevo_dsize = (nuevo_ancho, nuevo_alto)
img_rsize = cv2.resize(rot_img1, nuevo_dsize)

cv2.imshow("Ejercicio 4.1", img_rsize)
cv2.waitKey(0)
cv2.destroyAllWindows()