from PIL import Image, ImageEnhance
# Load the image
image = Image.open(r"C:\Users\gioes\Desktop\yellow.jpg")
# Enhance brightness
enhancer = ImageEnhance.Brightness(image)
enhanced_image = enhancer.enhance(1.5) # 1.0 is original, increase to make brighter
# Save the enhanced image
enhanced_image.save("enhanced_image.jpg")
enhanced_image.show()
print("Image enhancement complete!")
