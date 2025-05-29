import cv2
import numpy as np

vid_capture = cv2.VideoCapture('Recursos/slow_traffic_small.mp4')

feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

ret, old_frame = vid_capture.read()

old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

gray_float = np.float32(old_gray)
harris_corners = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)

harris_corners = cv2.dilate(harris_corners, None)

old_frame[harris_corners > 0.01 * harris_corners.max()] = [0, 100, 200]

p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

mask = np.zeros_like(old_frame)

while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, gray, p0, None, **lk_params)

    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            a, b, c, d = int(a), int(b), int(c), int(d)
            mask = cv2.line(mask, (a, b), (c, d), (200, 100, 0), 2)
            frame = cv2.circle(frame, (a, b), 5, (0, 100, 200), -1)

        img = cv2.add(frame, mask)

        cv2.imshow('Ejercicio 1', img)

        old_gray = gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

    key = cv2.waitKey(10)
    if key == ord('q'):
        break

vid_capture.release()
cv2.destroyAllWindows()