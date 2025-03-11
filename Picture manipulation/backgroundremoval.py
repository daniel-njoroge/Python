import cv2
import numpy as np
import os

def remove_background(image_path, output_path="apple_no_background.png"):
    try:
        # Read the image
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Could not read image at {image_path}")

        # Convert the image to HSV color space
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        #lower and upper bounds for green background color
        lower_green = np.array([36, 25, 25])        
        upper_green = np.array([86, 255, 255])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        
        mask_inv = cv2.bitwise_not(mask)
        
        foreground = cv2.bitwise_and(img, img, mask=mask_inv)

        transparent_background = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)  # 4-channel image
        transparent_background[:, :, 3] = 0 

       
        result = cv2.cvtColor(foreground, cv2.COLOR_BGR2BGRA) 
        result[mask_inv == 0] = [0, 0, 0, 0]
        
        cv2.imwrite(output_path, result)
        print(f"Background removed and saved to {output_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

image_file = "applewithbackground.jpg" 

if os.path.exists(image_file):
    remove_background(image_file)
else:
    print(f"Error: Image file '{image_file}' not found.")