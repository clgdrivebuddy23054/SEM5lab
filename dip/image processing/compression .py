from PIL import Image
# Load the image
image = Image.open(r"C:\Users\gioes\Downloads\WhatsApp Image 2025-06-26 at 11.18.47.jpeg")
# Compress the image and save it with reduced quality
compressed_image_path = "compressed_image.jpg"
image.save(compressed_image_path, "JPEG", quality=10) # Change
#quality as needed
# Show the compressed image
compressed_image = Image.open(compressed_image_path)
compressed_image.show()
print("Image compressed")
