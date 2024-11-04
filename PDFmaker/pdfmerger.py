import pikepdf
import os

def merge_pdfs(pdf_list, output_path):
    """Merge multiple PDF files into a single PDF."""
    # Create a new PDF object
    merged_pdf = pikepdf.new()

    for pdf_file in pdf_list:
        # Open each PDF file
        with pikepdf.open(pdf_file) as pdf:
            # Append each page to the merged PDF
            merged_pdf.pages.extend(pdf.pages)

    # Save the merged PDF
    merged_pdf.save(output_path)
    print(f"Merged PDF saved to: {output_path}")

# Paths to the PDF files you want to merge
pdf_files = [
    r"\input\001.pdf", 
    r"\input\002.pdf"
]

output_pdf = r"\output\merged_output.pdf"  # Output path

# Merge the PDF files
merge_pdfs(pdf_files, output_pdf)
