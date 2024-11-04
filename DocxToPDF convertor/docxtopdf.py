from docx2pdf import convert
import os

def convert_word_to_pdf(input_file, output_file):
    try:
        convert(input_file, output_file)
        print(f"Conversion successful! PDF saved at {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set the fixed path for the input and output files
    input_file = r"input.docx"
    output_file = r"output.pdf"

    convert_word_to_pdf(input_file, output_file)
