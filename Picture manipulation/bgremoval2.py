import cv2
import numpy as np

image = cv2.imread('apple.jpg')

mask = np.zeros(image.shape[:2], np.uint8)

bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)


rect = (50, 50, image.shape[1]-100, image.shape[0]-100)


cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)


mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')


apple = image * mask2[:, :, np.newaxis]


transparent_bg = np.zeros((apple.shape[0], apple.shape[1], 4), dtype=np.uint8)
transparent_bg[:, :, :3] = apple
transparent_bg[:, :, 3] = mask2 * 255  # Set alpha channel


cv2.imwrite('apple_extracted.png', transparent_bg)

print("Apple extracted and saved as 'apple_extracted.png'")