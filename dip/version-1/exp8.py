import cv2
# Read the image in grayscale
image = cv2.imread(r'C:\Users\gioes\Desktop\yellow.jpg', 0)
# Apply a blur effect
blurred_image = cv2.blur(image, (10, 10))
# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
