# 4. To create a program to display binary image of given image.

import cv2

# Step 1: Load the image
image = cv2.imread('resources/sd/family-sd-2.jpg')  # Replace with your image path

if image is None:
    print("Error: Image not found or unable to load.")
else:
# Step 2: Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply binary thresholding
# Pixels > 127 become white (255), others become black (0)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#ret, thresh = cv2.threshold(img, 127, 255, 0)

# Step 4: Display the binary image
    cv2.imshow('Binary Image', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
