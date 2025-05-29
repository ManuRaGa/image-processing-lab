import cv2
import numpy as np

cam = cv2.VideoCapture(0)

ret, prev_frame = cam.read()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fl_op = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 5, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(fl_op[..., 0], fl_op[..., 1])

    hsv = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)
    hsv[..., 1] = 255
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    flow_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('Ejercicio 2', flow_rgb)

    prev_gray = gray

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()