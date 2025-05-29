import cv2

img1 = "Foto1.jpg"
img2 = "Foto2.jpg"

img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

img1_b = cv2.GaussianBlur(img1, (5, 5), 0)
img2_b = cv2.GaussianBlur(img2, (5, 5), 0)

img_res = cv2.subtract(img1_b, img2_b)

cv2.imshow("Resta", img_res)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_thresh = cv2.threshold(img_res, 95, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Umbral", img_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

k3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask1 = cv2.dilate(img_thresh, k3, iterations=1)
cv2.imshow("Dilatacion", mask1)
mask2 = cv2.erode(img_thresh, k3, iterations=1)
cv2.imshow("Erosion", mask2)
mask3 = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, k3, iterations=1)
cv2.imshow("Apertura", mask3)
mask4 = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, k3, iterations=1)
cv2.imshow("Cierre", mask4)
cv2.waitKey(0)
cv2.destroyAllWindows()