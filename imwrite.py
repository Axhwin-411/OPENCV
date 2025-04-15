import cv2
img = cv2.imread("image.jpg")
cv2.imshow("im_write", img)
cv2.imwrite("im_write.png", img)
cv2.imwrite("im_write.tiff", img)
cv2.imshow("im_write.png", img)
cv2.imshow("im_write.tiff", img)
cv2.waitKey(0)