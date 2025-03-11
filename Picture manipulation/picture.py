import cv2 as cv
img = cv.imread("C:\Users\USER\Desktop\Python\applewithbackground.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0)