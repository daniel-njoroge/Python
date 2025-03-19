import cv2


image = cv2.imread('apple.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


threshold_value = gray_image.mean()


cv2.imshow('Img to Grayscale', gray_image)


print(f"Grayscale Threshold Value: {threshold_value}")


cv2.waitKey(0)
cv2.destroyAllWindows()