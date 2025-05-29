import cv2

def deteccion_movimiento(curr, prev):
    diff_frame = cv2.absdiff(curr, prev)
    cv2.imshow("Video", diff_frame)

    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    diff_frame = cv2.morphologyEx(diff_frame, cv2.MORPH_OPEN, kernel, iterations=1)

    cv2.imshow("Video", thresh_frame)
    return diff_frame

vid_capture = cv2.VideoCapture("C:/Users/HUAWEI/Desktop/L TRATAMIENTO/Manual/Practica 6 - Umbralizacion y operaciones morfologicas/Recursos/Calle.mp4")

prev_frame = None

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret:
        key = cv2.waitKey(10)
        if key == ord('q'):
            break
        prep_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        prep_frame = cv2.GaussianBlur(prep_frame, (3, 3), 0)

        if prev_frame is None:
            prev_frame = prep_frame
            continue

        mov_frame = deteccion_movimiento(prep_frame, prev_frame)
        prev_frame = prep_frame

        contours, _ = cv2.findContours(mov_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("Video", frame)

    else:
        break

vid_capture.release()
cv2.destroyAllWindows()