import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    CHESS_BOARD_DIM = (6, 4)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Encontrar las esquinas del tablero de ajedrez
    ret, corners = cv2.findChessboardCorners(gray, CHESS_BOARD_DIM)

    # Si son encontradas, refinar las esquinas y diujarlas en la imagen a color
    if ret:
        corners1 = cv2.cornerSubPix(gray, corners, (11, 11), (-1,-1), criteria)
        cv2.drawChessboardCorners(frame, CHESS_BOARD_DIM, corners1, ret)

    cv2.imshow('Ejercicio 1', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

