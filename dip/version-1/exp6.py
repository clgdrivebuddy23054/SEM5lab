import cv2
# Load the grayscale image
image = cv2.imread(r'C:\Users\gioes\Desktop\yellow.jpg',
cv2.IMREAD_GRAYSCALE)
# Check if the image is loaded
if image is None:
 print("Error: Image not found!")
else:
 # Set the zoom scale (1.0 = original size, > 1.0 = zoom in, < 1.0 =zoom out)
 scale = 1.5 # Change this value to zoom in or out
 # Zoom the image by resizing
 zoomed_image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
 # Display the original and zoomed images
 cv2.imshow('Original Image', image)
 cv2.imshow('Zoomed Image', zoomed_image)
 # Wait for a key press and close windows
 cv2.waitKey(0)
 cv2.destroyAllWindows()
