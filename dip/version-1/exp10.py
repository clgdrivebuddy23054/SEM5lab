from PIL import Image
# Load the image
image = Image.open(r"C:\Users\gioes\Desktop\yellow.jpg")
# Compress the image and save it with reduced quality
compressed_image_path = "compressed_image.jpg"
image.save(compressed_image_path, "JPEG", quality=10) # Change quality as needed
# Show the compressed image
compressed_image = Image.open(compressed_image_path)
compressed_image.show()
print("Image compressed")
