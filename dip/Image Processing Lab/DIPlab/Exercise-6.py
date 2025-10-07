# 6. To create a program that reads a gray scale image and rotate the image.

import cv2

# Load the image in grayscale
gray_img = cv2.imread('Resources/sd/people-sd-1.jpg', cv2.IMREAD_GRAYSCALE)

# Get image dimensions
(h, w) = gray_img.shape

# Define rotation center (usually the center of the image)
center = (w // 2, h // 2)

# Define rotation angle (e.g., 45 degrees)
angle = 75

# Get the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)

# Apply the rotation
rotated_img = cv2.warpAffine(gray_img, rotation_matrix, (w, h))

# Display the original and rotated images
cv2.imshow('Original Grayscale Image', gray_img)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()