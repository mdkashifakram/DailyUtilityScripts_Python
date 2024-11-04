import os
from PIL import Image

def images_to_pdf(source_folder, output_pdf):
    # Ensure the source folder exists, create it if not
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)
        print(f"Created folder: {source_folder}")
        return

    # List to hold all images
    image_list = []

    # Get all image files in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            # Full path to the image file
            img_path = os.path.join(source_folder, filename)

            # Open the image
            img = Image.open(img_path)

            # Convert to RGB (required for PDF conversion)
            img = img.convert('RGB')

            # Append the image to the list
            image_list.append(img)

    # If no images are found, stop execution
    if not image_list:
        print(f"No images found in '{source_folder}'.")
        return

    # Ensure the output folder exists, create it if not
    output_folder = os.path.dirname(output_pdf)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # Save the images as a single PDF
    image_list[0].save(output_pdf, save_all=True, append_images=image_list[1:])
    print(f"PDF created successfully: {output_pdf}")

# Define the source folder path and output PDF file name
source_folder = os.path.expanduser(r"\input")
output_pdf = os.path.expanduser(r"\output\merged_images.pdf")

# Run the conversion function
images_to_pdf(source_folder, output_pdf)
