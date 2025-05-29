import cv2
import numpy as np

cam = cv2.VideoCapture(0)

apply_sobel = False
apply_prewitt = False
apply_roberts = False
apply_canny = False

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    if apply_sobel:
        frame = cv2.Sobel(src= frame, ddepth=-1, dx=1, dy=1, ksize=5)

    if apply_prewitt:
        prew_kernel_x = np.array([[-1, 0, 1],
                                [-1, 0, 1],
                                [-1, 0, 1]])

        prew_kernel_y = np.array([[-1, -1, -1],
                                [0, 0, 0],
                                [1, 1, 1]])

        der_x = cv2.filter2D(frame, cv2.CV_64F, prew_kernel_x)
        der_y = cv2.filter2D(frame, cv2.CV_64F, prew_kernel_y)

        absX = cv2.convertScaleAbs(der_x)
        absY = cv2.convertScaleAbs(der_y)

        frame = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    if apply_roberts:
        rob_kernel_x = np.array([[1, 0],
                                [0, -1]])

        rob_kernel_y = np.array([[0, 1],
                                [-1, 0]])

        der_x = cv2.filter2D(frame, cv2.CV_64F, rob_kernel_x)
        der_y = cv2.filter2D(frame, cv2.CV_64F, rob_kernel_y)

        absX = cv2.convertScaleAbs(der_x)
        absY = cv2.convertScaleAbs(der_y)

        frame = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    if apply_canny:
        frame = cv2.Canny(image=frame, threshold1=100, threshold2=200)

    cv2.imshow("Ejercicio 5.2", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('n'):
        apply_sobel = False
        apply_prewitt = False
        apply_roberts = False
        apply_canny = False
    elif key == ord('s'):
        apply_sobel = True
        apply_prewitt = False
        apply_roberts = False
        apply_canny = False
    elif key == ord('p'):
        apply_prewitt = True
        apply_sobel = False
        apply_roberts = False
        apply_canny = False
    elif key == ord('r'):
        apply_roberts = True
        apply_prewitt = False
        apply_sobel = False
        apply_canny = False
    elif key == ord('c'):
        apply_canny = True
        apply_sobel = False
        apply_roberts = False
        apply_prewitt = False

cam.release()
cv2.destroyAllWindows()