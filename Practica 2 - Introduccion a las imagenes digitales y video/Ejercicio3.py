import cv2

cam = cv2.VideoCapture(0)

while (cam.isOpened()):
    ret, frame = cam.read()
    if ret:
        cv2.imshow("Ejercicio 2.3", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()