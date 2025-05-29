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

valores_monedas = {
    (3500, 4500): 0.05,   # Moneda de 5 centavos
    (4500, 6000): 0.10,   # Moneda de 10 centavos
    (6000, 6500): 0.20,   # Moneda de 20 centavos
    (7000, 8000): 0.50,   # Moneda de 50 centavos
    (6500, 7000): 1.0,    # Moneda de 1 peso
    (8000, 9000): 2.0,    # Moneda de 2 pesos
    (9000, 9600): 5.0,    # Moneda de 5 pesos
    (9600, 10000): 10.0,  # Moneda de 10 pesos
    (10000, 11000): 20.0  # Moneda de 20 pesos
}

monedas_detectadas = []
valor_total = 0

img_countours = img_color.copy()
cv2.drawContours(img_countours, contours, -1, (0, 255, 0), 2)

for contour in contours:
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        area = cv2.contourArea(contour)

        valor_moneda = 0
        for (min_area, max_area), valor in valores_monedas.items():
            if min_area <= area < max_area:
                valor_moneda = valor
                break

        monedas_detectadas.append({"centroide": (cx, cy), "area": area, "valor": valor_moneda})
        valor_total += valor_moneda

        cv2.circle(img_countours, (cx, cy), 5, (0, 0, 255), -1)

        cv2.putText(img_countours, f"${valor_moneda}", (cx - 20, cy - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

print(f"Cantidad de monedas detectadas: {len(monedas_detectadas)}")
print(f"Valor total en la imagen: ${valor_total}")

plt.figure(figsize=(15, 15))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_countours, cv2.COLOR_BGR2RGB))
plt.title(f"Contornos y Valores - Total: ${valor_total}")
plt.axis("off")

plt.show()
