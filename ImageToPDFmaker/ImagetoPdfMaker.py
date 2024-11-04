import os
from PIL import Image

# Paths for the input folder containing images and the output folder for the PDF
input_folder = r"\input"
output_folder = r"\output"
output_pdf = os.path.join(output_folder, "merged_images.pdf")

# Get a list of image file names from the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith(('png', 'jpg', 'jpeg'))]

# Sort the images (if necessary) based on file names
image_files.sort()

# Open the images
image_list = []
for file_name in image_files:
    file_path = os.path.join(input_folder, file_name)
    image = Image.open(file_path).convert("RGB")  # Convert images to RGB format
    image_list.append(image)

# Save the first image and append the rest as a PDF
if image_list:
    first_image = image_list[0]
    first_image.save(output_pdf, save_all=True, append_images=image_list[1:])

print(f"PDF created and saved at {output_pdf}")
