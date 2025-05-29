import cv2

img3 = cv2.imread('Recursos\Hollow Knight.jpg', cv2.IMREAD_COLOR)

escala = 0.6
ancho = int(img3.shape[1] * escala)
alto = int(img3.shape[0] * escala)
img3 = cv2.resize(img3, (ancho, alto), interpolation=cv2.INTER_AREA)

window = 'Ejercicio 4.3'
contrast = 10
max_contrast = 100
brightness = 0
max_brightness = 100

def change_contrast(val):
    global contrast
    contrast = val/1000
    perform_operation()

def change_brightness(val):
    global brightness
    brightness = val/100
    perform_operation()

def perform_operation():
    img = img3*contrast + brightness
    cv2.imshow(window, img)

cv2.imshow(window, img3)
cv2.createTrackbar('Contrast', window, contrast, max_contrast, change_contrast)
cv2.createTrackbar('Brightness', window, brightness, max_brightness, change_brightness)
cv2.waitKey(0)