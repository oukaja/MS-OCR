import cv2
import numpy as np

filename = 'cin.jpg'
W = 1000.
oriimg = cv2.imread(filename)
height, width, depth = oriimg.shape
imgScale = W/width
newX,newY = oriimg.shape[1]*imgScale, oriimg.shape[0]*imgScale
newimg = cv2.resize(oriimg,(int(newX),int(newY)))
cv2.imshow("Show by CV2",newimg)
cv2.waitKey(0)
cv2.imwrite("resizeimg.jpg",newimg)

r = cv2.selectROI(newimg)

imCrop = newimg[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

cv2.imshow("Image", imCrop)
cv2.waitKey(0)

cv2.imwrite("cropimg.jpg",imCrop)
