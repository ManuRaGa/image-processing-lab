import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

tol = 7
showing = False

def mouseFunc(evento, x, y, flags, img):
    global showing
    if evento == cv2.EVENT_LBUTTONDOWN:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        os.system("cls")
        mat, sat, val = hsv[y, x]
        print(f'[{mat}, {sat}, {val}]')
        if (mat - tol) >= 0 and (mat + tol) <= 255:
            lower = np.array((mat - tol, 10, 50), np.uint8)
            upper = np.array((mat + tol, 255, 255), np.uint8)
            mascara = cv2.inRange(hsv, lower, upper)
        else:
            lower = np.array((0, 10, 50), np.uint8)
            upper = np.array((0 + tol, 255, 255), np.uint8)
            bin_img = cv2.inRange(hsv, lower, upper)

            lower = np.array((255 - tol, 10, 50), np.uint8)
            upper = np.array((255 + tol, 255, 255), np.uint8)
            bin2_img = cv2.inRange(hsv, lower, upper)

            mascara = cv2.bitwise_or(bin_img, bin2_img)

        res = cv2.bitwise_and(img, img, mask = mascara)
        cv2.imshow("Segmentacion", res)
        showing = True

    if evento == cv2.EVENT_RBUTTONUP:
        if showing:
            os.system("cls")
            print("Imagen Original")
            cv2.destroyWindow("Segmentacion")

def main():
    img = cv2.imread("C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 3 - Espacios de color y segmentacion de color/Imagenes/Stardew Valley_boda.jpg", cv2.IMREAD_COLOR)
    cv2.namedWindow('Colores')
    cv2.setMouseCallback('Colores', mouseFunc, img)

    while True:
        cv2.imshow('Colores', img)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()