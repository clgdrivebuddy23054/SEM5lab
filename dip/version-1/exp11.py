import cv2
import matplotlib.pyplot as plt
def segment_image(image_path, threshold_value=127):
 # Read the image in grayscale
 image = cv2.imread(r"C:\Users\gioes\Desktop\yellow.jpg", cv2.IMREAD_GRAYSCALE)
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
# Example usage
segment_image(r'C:\Users\Admin\Desktop\bunch.jpg',
threshold_value=127)
