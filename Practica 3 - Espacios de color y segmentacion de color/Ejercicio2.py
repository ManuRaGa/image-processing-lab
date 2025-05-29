import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb = cv2.imread("C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 3 - Espacios de color y segmentacion de color/Imagenes/Pez Dorado3.jpg", cv2.IMREAD_COLOR)

img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)

h = cv2.add(v, 30)

img_hsv = cv2.merge([h, s, v])
img_new = cv2.cvtColor(img_hsv, cv2.COLOR_BGR2RGB)

mostrar = True
while mostrar:
    plt.figure(figsize=(1, 4))
    cv2.imshow("Imagen Original", img_rgb)
    cv2.imshow("Imagen Modificada", img_new)
    k = cv2.waitKey(1)
    if k == ord('q'):
        mostrar = False

cv2.destroyAllWindows()