import os
from PIL import Image

# Function to compress and reduce image size
def compress_image(input_image_path, output_image_path, quality=85):
    # Open an image file
    with Image.open(input_image_path) as img:
        # Save the image with a reduced file size
        img.save(output_image_path, optimize=True, quality=quality)

# Function to reduce image size to less than 1MB
def reduce_image_size(input_folder, output_folder, max_size_mb=0.20):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)

            # Compress the image with a loop until it's less than 1MB
            quality = 85  # Start with default quality
            compress_image(input_image_path, output_image_path, quality=quality)

            while os.path.getsize(output_image_path) > max_size_mb * 1024 * 1024:
                quality -= 6  # Reduce quality by 5% on each loop
                compress_image(input_image_path, output_image_path, quality=quality)
                
                if quality < 6:  # Stop if the quality goes too low
                    print(f"Could not compress {filename} enough")
                    break

            # Check final size
            final_size = os.path.getsize(output_image_path) / (1024 * 1024)
            print(f"{filename}: {final_size:.2f} MB (compressed)")

# Define input and output folders
input_folder = r'\input'
output_folder = r'\output'

# Reduce the size of images in the folder
reduce_image_size(input_folder, output_folder)
