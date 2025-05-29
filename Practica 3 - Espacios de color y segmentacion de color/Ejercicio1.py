import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb = cv2.imread("C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 3 - Espacios de color y segmentacion de color/Imagenes/Colores.jpg", cv2.IMREAD_COLOR)

img_cmy = 1- (img_rgb/255)

mostrar = True
while mostrar:
    cv2.imshow("Imagen RGB", img_rgb)
    cv2.imshow("Imagen CMY", img_cmy)
    k = cv2.waitKey(0)
    if k == ord('q'):
        mostrar = False
        cv2.destroyAllWindows()
