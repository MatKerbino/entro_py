from PIL import Image

image = Image.open('106220.png')

print(f"Current size: {image.size}")

resized_image = image.resize((50, 50))

resized_image.save('Plush-500.jpeg')
