# 8. To create a program that reads a gray scale image and zoom in or zoom out the
#  image.

import cv2

# Load the grayscale image
img = cv2.imread('Resources/sd/family-sd-2.jpg', cv2.IMREAD_GRAYSCALE)

# ----- Zoom In (e.g., 2x enlargement) -----
zoom_in = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

# ----- Zoom Out (e.g., 0.5x reduction) -----
zoom_out = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display results
cv2.imshow('Original Image', img)
cv2.imshow('Zoomed In Image', zoom_in)
cv2.imshow('Zoomed Out Image', zoom_out)

cv2.waitKey(0)
cv2.destroyAllWindows()