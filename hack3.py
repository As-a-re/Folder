from PIL import Image
import os

folder_path = "C:\Games"

image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for image_file in image_files:
    try:
        image_path = os.path.join(folder_path, image_file)
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"Error displaying image {image_file}: {e}")
