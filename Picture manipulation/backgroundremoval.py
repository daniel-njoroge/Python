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

        # Define the lower and upper bounds for the background color (adjust these values as needed)
        # These values work reasonably well for a likely green background.
        lower_green = np.array([36, 25, 25])
        upper_green = np.array([86, 255, 255])

        # Create a mask to isolate the background
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Invert the mask to isolate the foreground
        mask_inv = cv2.bitwise_not(mask)

        # Extract the foreground
        foreground = cv2.bitwise_and(img, img, mask=mask_inv)

        # Create a transparent background with an alpha channel
        transparent_background = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)  # Create a 4-channel image
        transparent_background[:, :, 3] = 0  # Initialize alpha channel to 0

        # Combine the foreground with the transparent background
        result = cv2.cvtColor(foreground, cv2.COLOR_BGR2BGRA) #Convert foreground to BGRA (adds alpha)
        result[mask_inv == 0] = [0, 0, 0, 0] #set background to transparent.

        # Save the result as a PNG with transparency
        cv2.imwrite(output_path, result)
        print(f"Background removed and saved to {output_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
image_file = "applewithbackground.jpg" #Ensure this file exists in the same directory, or provide full path.

if os.path.exists(image_file):
    remove_background(image_file)
else:
    print(f"Error: Image file '{image_file}' not found.")