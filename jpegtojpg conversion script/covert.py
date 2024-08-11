import os
from PIL import Image

def convert_jpeg_to_jpg(source_folder):
    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Get all JPEG files in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpeg"):
            # Full path to the original JPEG file
            jpeg_path = os.path.join(source_folder, filename)
            
            # Define the new file name with .jpg extension
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(source_folder, new_filename)

            # Open the JPEG image and save it as a JPG
            with Image.open(jpeg_path) as img:
                img.save(jpg_path, "JPEG")
            
            print(f"Converted: {jpeg_path} to {jpg_path}")

# Define the source folder path (update this to your local desktop folder path)
source_folder = os.path.expanduser("~/Desktop/your-folder-name")

# Run the conversion function
convert_jpeg_to_jpg(source_folder)
