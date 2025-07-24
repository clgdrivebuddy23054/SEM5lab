from PIL import Image 
# Load the grayscale image 
img = Image.open(r"requirements\requirement.png").convert('L')  
# 'L' mode for grayscale 
# Rotate the image by 45 degrees 
rotated_img = img.rotate(45, expand=True) 
# Save the rotated image 
rotated_img.save('rotated_image.jpg') 
# Show the original and rotated images 
img.show() 
rotated_img.show()