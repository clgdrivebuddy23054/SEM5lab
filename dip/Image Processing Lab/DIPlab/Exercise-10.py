# 10.  To create a program that reads a gray scale image and crop the image.

import cv2

# Load the grayscale image
img = cv2.imread('Resources/sd/table-sd-1.jpg', cv2.IMREAD_GRAYSCALE)

# Define crop region: [startY:endY, startX:endX]
# Example: Crop a 100x100 region starting from (50, 50)
cropped_img = img[50:150, 50:150]

# Display original and cropped images
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()