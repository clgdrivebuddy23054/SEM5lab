# 5. To create a program to display greyscale image of given image.

import cv2

# Load the original image
image = cv2.imread('Resources/sd/nature-sd-1.jpg')  # Replace with your image path

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display both original and grayscale images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()