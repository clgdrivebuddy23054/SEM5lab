import cv2 
# Load the image in grayscale 
image = cv2.imread( r"requirements\requirement.png",cv2.IMREAD_GRAYSCALE) 
# Check if the image is loaded successfully 
if image is None: 
    print("Error loading image.") 
if image is None: 
    print("Error loading image.") 
else: 
    # Flip the image horizontally 
    flipped_image = cv2.flip(image, 1)  # 1 for horizontal flip 
  
    # Display the original and flipped images 
    cv2.imshow('Original Image', image) 
    cv2.imshow('Flipped Image', flipped_image) 
  
    # Save the flipped image to a file 
    cv2.imwrite('flipped_image.jpg', flipped_image) 
  
    # Wait for a key press and close all windows 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 