# 19. To create a program for image segmentation.

import cv2

# Load the image in grayscale
img = cv2.imread('Resources/sd/buffalo-sd-1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply binary thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Find contours from the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a copy of the original image
segmented = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(segmented, contours, -1, (0, 255, 0), 2)

# Display results
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Segmented Image', segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()