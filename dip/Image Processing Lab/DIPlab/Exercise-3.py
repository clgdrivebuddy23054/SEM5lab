# 3. To create a program to read and show an image.

import cv2

# Step 1: Read the image
image = cv2.imread('Resources/sd/flowers-sd-1.jpg')  # Replace with your actual image path

# Step 2: Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Step 3: Display the image in a window
    cv2.imshow('Displayed Image', image)

    # Step 4: Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

