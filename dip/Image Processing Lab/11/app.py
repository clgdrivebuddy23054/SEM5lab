import cv2 
import matplotlib.pyplot as plt

def segment_image(image_path, threshold_value=127): 
    # Read the image in grayscale 
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"❌ Error: Could not load image from path: {image_path}")
        return
  
    # Apply binary thresholding 
    _, segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY) 
  
    # Display original and segmented images 
    plt.figure(figsize=(10, 5)) 
    plt.subplot(1, 2, 1) 
    plt.title('Original Image') 
    plt.imshow(image, cmap='gray') 
    plt.axis('off') 
  
    plt.subplot(1, 2, 2) 
    plt.title('Segmented Image') 
    plt.imshow(segmented_image, cmap='gray') 
    plt.axis('off') 
  
    plt.show() 

segment_image('C:/23054-AI-051/Image Processing Lab/requirements/requirement.png', threshold_value=127)

