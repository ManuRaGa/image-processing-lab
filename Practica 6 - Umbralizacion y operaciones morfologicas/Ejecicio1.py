import cv2

cam = cv2.VideoCapture(0)

while (cam.isOpened()):
    ret, frame = cam.read()
    if ret:
        cv2.imshow("Ejercicio 6.1", frame)
        key = cv2.waitKey(1)
        if key == ord('f'):
            cv2.imwrite("Foto1.jpg", frame)
        if key == ord('g'):
            cv2.imwrite("Foto2.jpg", frame)
        if key == ord('q'):
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()