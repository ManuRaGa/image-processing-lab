import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises y en color
img_path = "C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 7 - Deteccion de contornos/Imagenes/Monedas.png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)

# Aplicar suavizado para reducir ruido
img_blurr = cv2.GaussianBlur(img, (5, 5), 0)

# Umbralización para obtener imagen binaria
_, thersh = cv2.threshold(img_blurr, 10, 255, cv2.THRESH_BINARY)

# Operación morfológica para cerrar pequeños huecos
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thersh, cv2.MORPH_CLOSE, kernel, iterations=1)

# Encontrar contornos
contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos sobre la imagen a color
img_countours = img_color.copy()
cv2.drawContours(img_countours, contours, -1, (0, 255, 0), 2)

# Lista para almacenar áreas de las monedas detectadas
areas_detectadas = []

# Calcular y dibujar centroides de cada contorno
for i, contour in enumerate(contours):
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        # Calcular área de la moneda
        area = cv2.contourArea(contour)
        areas_detectadas.append(area)

        # Dibujar centroide y mostrar área en la imagen
        cv2.circle(img_countours, (cx, cy), 5, (0, 0, 255), -1)
        cv2.putText(img_countours, f"{int(area)}", (cx - 20, cy - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# Mostrar la cantidad de monedas detectadas y sus áreas
print(f"Cantidad de monedas detectadas: {len(areas_detectadas)}")
print("Áreas de las monedas detectadas:", areas_detectadas)

# Mostrar imágenes
plt.figure(figsize=(15, 15))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_countours, cv2.COLOR_BGR2RGB))
plt.title("Contornos y Áreas")
plt.axis("off")

plt.show()