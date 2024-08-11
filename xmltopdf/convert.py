import xml.etree.ElementTree as ET
from xhtml2pdf import pisa

def xml_to_html(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Start building the HTML string
    html = '<html><head><meta charset="utf-8"/><title>XML to PDF</title></head><body>'
    
    def traverse_node(node, html):
        tag = node.tag
        text = node.text.strip() if node.text else ''
        html += f'<h2>{tag}</h2>'
        if text:
            html += f'<p>{text}</p>'
        for child in node:
            html = traverse_node(child, html)
        return html
    
    html = traverse_node(root, html)
    html += '</body></html>'
    return html

def convert_html_to_pdf(source_html, output_filename):
    with open(output_filename, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(source_html, dest=result_file)
    return pisa_status.err

if __name__ == "__main__":
    # Paths to your XML file and desired PDF output
    xml_file = 'INPUT_PATH'
    pdf_file = 'OUTPUTPATH'

    
    # Convert XML to HTML
    html_content = xml_to_html(xml_file)
    
    # Convert HTML to PDF
    result = convert_html_to_pdf(html_content, pdf_file)
    
    if result == 0:
        print("PDF generated successfully.")
    else:
        print("Error generating PDF.")
