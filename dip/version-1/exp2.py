import cv2
# Load the image (replace 'image_path.jpg' with the path to your image file)
image = cv2.imread(r'C:\Users\gioes\Desktop\yellow.jpg')
# Check if the image was successfully loaded
if image is None:
 print("Error: Image not found.")
else:
 # Convert the image to grayscale
 gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 # Display the grayscale image
 cv2.imshow('Grayscale Image', gray_image)
 # Wait indefinitely until a key is pressed
 cv2.waitKey(0)
 # Close all OpenCV windows
 cv2.destroyAllWindows()
