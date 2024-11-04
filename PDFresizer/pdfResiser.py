import pikepdf
import os

def get_file_size(file_path):
    """Get the file size in bytes."""
    return os.path.getsize(file_path)

def compress_images(pdf, quality=75):
    """Compress images in the PDF."""
    for page in pdf.pages:
        for img in page.images:
            # Load the image
            image = pdf.pages[page.objgen].images[img]
            # Compress the image and update the original
            image.compress(quality=quality)

def resize_pdf(input_path, output_path, target_size_mb):
    # Calculate the target size in bytes
    target_size_bytes = target_size_mb * 1024 * 1024

    # Get the original size of the PDF
    original_size = get_file_size(input_path)

    # If original size is less than or equal to the target, no need to resize
    if original_size <= target_size_bytes:
        print("The PDF is already under the target size.")
        return

    # Open the PDF file
    with pikepdf.open(input_path) as pdf:
        # Create a new PDF object
        new_pdf = pikepdf.new()

        # Compress images before copying
        compress_images(pdf)

        # Copy each page
        for page in pdf.pages:
            new_pdf.pages.append(page)

        # Save the new PDF
        new_pdf.save(output_path)

    # Get the new size of the PDF
    new_size = get_file_size(output_path)
    print(f"Original size: {original_size / (1024 * 1024):.2f} MB")
    print(f"New size: {new_size / (1024 * 1024):.2f} MB")

# Paths
input_pdf = r"\input\filename.pdf"  # Replace with your file name
output_pdf = r"\output\yourfile_resized.pdf"  # Output path

# Resize the PDF to under 1 MB
resize_pdf(input_pdf, output_pdf, target_size_mb=1)
