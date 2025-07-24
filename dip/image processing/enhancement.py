from PIL import Image, ImageEnhance
# Load the image
image = Image.open(r"C:\Users\gioes\Downloads\WhatsApp Image 2025-06-26 at 11.18.47.jpeg")
# Enhance brightness
enhancer = ImageEnhance.Brightness(image)
enhanced_image = enhancer.enhance(1.5) # 1.0 is original, increase
#to make brighter
# Save the enhanced image
enhanced_image.save("enhanced_image.jpg")
enhanced_image.show()
print("Image enhancement complete!")
