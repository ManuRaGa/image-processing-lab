import cv2

cam = cv2.VideoCapture(0)

apply_blur = False
apply_gauss = False
apply_med = False

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    if apply_blur:
        frame = cv2.blur(src=frame, ksize=(51, 51))

    if apply_gauss:
        frame = cv2.GaussianBlur(src=frame, ksize=(51, 51), sigmaX=0, sigmaY=0)

    if apply_med:
        frame = cv2.medianBlur(frame, ksize=51)

    cv2.imshow("Ejercicio 5.1", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('n'):
        apply_blur = False
        apply_gauss = False
        apply_med = False
    elif key == ord('b'):
        apply_blur = True
        apply_gauss = False
        apply_med = False
    elif key == ord('g'):
        apply_gauss = True
        apply_blur = False
        apply_med = False
    elif key == ord('m'):
        apply_med = True
        apply_blur = False
        apply_gauss = False

cam.release()
cv2.destroyAllWindows()