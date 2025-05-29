import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

CHESS_BOARD_DIM = (6, 4)
# tamaño de cuadrado en tablero de ajedrez
SQUARE_SIZE = 20  # milimetros

# preparar los puntos del objeto, como (0,0,0), (1,0,0), (2,0,0) ....,(7,5,0)
obj_3D = np.zeros((CHESS_BOARD_DIM[0] * CHESS_BOARD_DIM[1], 3), np.float32)
obj_3D[:, :2] = np.mgrid[0 : CHESS_BOARD_DIM[0], 0 : CHESS_BOARD_DIM[1]].T.reshape(-1, 2)
obj_3D *= SQUARE_SIZE
print(obj_3D)

# Cambiar dimensiones de tablero en base a cual se este utilizando
CHESS_BOARD_DIM = (7, 5)

# Matrices para almacenar los puntos objeto y los puntos imagen de todas las imágenes.
obj_points_3D = []  # Puntos 3D en el espacio del mundo real
img_points_2D = []  # Puntos 2D en el plano de la imagen.

# La ruta del directorio de imágenes
image_dir_path = "images"

files = os.listdir(image_dir_path)
for file in files:
    imagePath = os.path.join(image_dir_path, file)

    image = cv2.imread(imagePath)
    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(image, CHESS_BOARD_DIM, None)
    if ret == True:
        obj_points_3D.append(obj_3D)
        corners2 = cv2.cornerSubPix(grayScale, corners, (3, 3), (-1, -1), criteria)
        img_points_2D.append(corners2)

print(img_points_2D)

print(obj_points_3D)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points_3D, img_points_2D, grayScale.shape[::-1], None, None)

# matriz de parametros intrinsecos de la cámara
print(mtx)

img_dist = cv2.imread('Fotos/1.png')
h,  w = img_dist.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

# nueva matriz de parametros intrinsecos de la cámara
print(newcameramtx)

# corregir distorcion
dst = cv2.undistort(img_dist, mtx, dist, None, newcameramtx)

def plot_img(images, titles):
  fig, axs = plt.subplots(nrows = 1, ncols = len(images), figsize = (15, 15))
  for i, p in enumerate(images):
    axs[i].imshow(cv2.cvtColor(p, cv2.COLOR_BGR2RGB))
    axs[i].set_title(titles[i])
    axs[i].axis('off')
  plt.show()

# recortar la imagen
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
imagenes = [img_dist, dst]
titulos = ['Imagen distorcionada', 'Imagen corregida']
plot_img(imagenes, titulos)