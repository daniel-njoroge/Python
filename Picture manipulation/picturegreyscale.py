import cv2

image = cv2.imread('applewithbackground.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value = gray_image.mean()

print(f"Threshold Value: {threshold_value}")

cv2.imshow('Grayscale Window', gray_image)
cv2.waitKey(0)



cv2.destroyAllWindows()