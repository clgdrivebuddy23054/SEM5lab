import cv2 
# Load the image 
image = cv2.imread(r"requirements\krishna.jpg") 
#Replace 'image_path.jpg' with the path to your image file 
# Check if the image was successfully loaded 
if image is None: 
    print("Error: Image not found.") 
else: 
# Display the image 
    cv2.imshow('Displayed Image', image) 
# Wait indefinitely until a key is pressed 
cv2.waitKey(0) 
# Close all OpenCV windows 
cv2.destroyAllWindows()