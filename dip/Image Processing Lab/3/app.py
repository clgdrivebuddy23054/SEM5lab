import cv2 
 
# Load the image (replace 'image_path.jpg' with the path to 
image = cv2.imread(r"requirements\requirement.png") 
 # Check if the image was successfully loaded 
if image is None: 
    print("Error: Image not found.") 
else: 
    # Convert the image to grayscale 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
 
    # Apply binary thresholding 
    # The second argument is the threshold value, and the third 
#is the max value to use with the THRESH_BINARY option 
    _, binary_image = cv2.threshold(gray_image, 127, 255, 
cv2.THRESH_BINARY) 
 
    # Display the binary image 
    cv2.imshow('Binary Image', binary_image) 
 
    # Wait indefinitely until a key is pressed 
    cv2.waitKey(0) 
 
    # Close all OpenCV windows 
    cv2.destroyAllWindows() 