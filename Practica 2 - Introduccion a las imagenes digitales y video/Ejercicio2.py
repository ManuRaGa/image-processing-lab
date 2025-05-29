#Ejercicio 2

import cv2

vidcap = cv2.VideoCapture("C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 2 - Introduccion a las imagenes digitales y video/Recursos/traffic.mp4")
while (vidcap.isOpened()):
    ret, frame = vidcap.read()
    if ret:
        cv2.imshow("Ejercicio 2.2", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break

vidcap.release()
cv2.destroyAllWindows()