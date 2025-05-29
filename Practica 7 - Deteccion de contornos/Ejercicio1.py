import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = "C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 7 - Deteccion de contornos/Imagenes/Monedas.png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)

img_blurr = cv2.GaussianBlur(img, (5, 5), 0)
_, thersh = cv2.threshold(img_blurr, 10, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thersh, cv2.MORPH_CLOSE, kernel, iterations=1)

contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

num_monedas = len(contours)
print(f"Numero de monedas: {num_monedas}")

img_countours = img_color.copy()
cv2.drawContours(img_countours, contours, -1, (0, 255, 0), 2)

for contour in contours:
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cv2.circle(img_countours, (cx, cy), 5, (0, 0, 255), -1)

plt.figure(figsize=(15, 15))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_countours, cv2.COLOR_BGR2RGB))
plt.title("Contornos y Centroides")
plt.axis("off")

plt.show()
