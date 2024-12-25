import os
from datetime import datetime
import csv

def get_edi_file(input_folder):
    # Scan the input folder for any .edi file
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.edi'):
            return os.path.join(input_folder, file_name)
    raise FileNotFoundError("No .edi file found in the specified input folder.")

def generate_multiple_files(base_invoice, base_order, num_files, input_folder=".", output_folder="generated_files"):
    # Automatically find the .edi file in the input folder
    input_file_path = get_edi_file(input_folder)

    # Creating output folder to store generated EDI files.
    os.makedirs(output_folder, exist_ok=True)

    base_invoice_prefix = ''.join(filter(str.isalpha, base_invoice))  # Extract the prefix (e.g., "DSD")
    base_invoice_num = int(''.join(filter(str.isdigit, base_invoice)))  # Extract the numeric part (e.g., 1)
    base_order_num = int(base_order)

    # Read the contents of the input EDI file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Timestamp for file names
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the item data with MIN and BARCODE values
    items_data = [
        {"MIN": "MIN1", "BARCODE": "BARCODE1"},
        {"MIN": "MIN2", "BARCODE": "BARCODE2"},
        {"MIN": "MIN3", "BARCODE": "BARCODE3"},
        {"MIN": "MIN4", "BARCODE": "BARCODE4"},
        {"MIN": "MIN5", "BARCODE": "BARCODE5"}
    ]

    # Prepare a list to hold delivery info records
    delivery_info_records = []

    # Generate multiple EDI files and build delivery info entries
    for i in range(num_files):
        # Increment and format invoice and order numbers
        current_invoice = f"{base_invoice_prefix}{base_invoice_num + i:04}"  # Invoice number with prefix and padding
        current_invoice_formatted = current_invoice.ljust(40)
        current_order = str(base_order_num + i).zfill(10)  # EDI format: 10-character padded order number
        delivery_order = str(base_order_num + i)  # Delivery info format: unpadded order number

        # Update the EDI file content with the current invoice and order numbers
        updated_lines = []
        for line in lines:
            if line.startswith("THEAD"):
                line = line[:31] + current_invoice_formatted + line[71:]  # Update invoice number
                line = line[:101] + current_order + line[111:]  # Update order number
            updated_lines.append(line)

        # Construct the EDI file name with timestamp and sequence number
        edi_file_name = f"{timestamp}{i+1:07}.edi"[:25]
        edi_file_path = os.path.join(output_folder, edi_file_name)

        # Write the updated content to the EDI file
        with open(edi_file_path, 'w') as file:
            file.writelines(updated_lines)

        # Append each item as a separate line in delivery info records
        for item_data in items_data:
            delivery_info_records.append([
                delivery_order,          # DELIVERY_REF_ID, using unpadded order number
                "SUPPLIER_NUMBER",                  # SUPPLIER
                "LOCATION",                   # LOCATION
                "24-Oct-24",             # DELIVERY_DATE
                item_data["MIN"],        # MIN, as per specified data
                "",                      # PIN
                item_data["BARCODE"],    # BARCODE, as per specified data
                "20"                     # QUANTITY
            ])

        # Print progress
        print(f"File {i+1}/{num_files} generated: {edi_file_path}")

    # Write all delivery info records to a single CSV file
    delivery_info_file_name = f"{timestamp}_DeliveryInfo.csv"
    delivery_info_file_path = os.path.join(output_folder, delivery_info_file_name)

    with open(delivery_info_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow([
            "DELIVERY_REF_ID", "SUPPLIER", "LOCATION", "DELIVERY_DATE",
            "MIN", "PIN", "BARCODE", "QUANTITY"
        ])
        # Write records
        writer.writerows(delivery_info_records)

    print(f"Delivery info file generated: {delivery_info_file_path}")

# Input parameters
base_invoice_number = input("Enter the base invoice number (e.g., DSD0001): ")
base_order_number = input("Enter the base order number (e.g., 227): ")
num_files_to_generate = int(input("Enter the number of files to generate (e.g., 5000): "))

# Run the function
generate_multiple_files(base_invoice_number, base_order_number, num_files_to_generate)
