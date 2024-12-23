import qrcode
import os

# Directory to save QR codes
output_dir = "qr_codes"
os.makedirs(output_dir, exist_ok=True)


# Sample inventory data
inventory = {
    "ITEM001": {"name": "Fertilizer Bag", "quantity": 50, "location": "Aisle 3"},
    "ITEM002": {"name": "Seed Pack", "quantity": 120, "location": "Aisle 5"},
    "ITEM003": {"name": "Tractor Part", "quantity": 15, "location": "Aisle 1"},
    "ITEM004": {"name": "Irrigation Pipe", "quantity": 75, "location": "Aisle 6"},
}

# Function to generate QR codes for inventory items
def generate_qr_codes(inventory, output_dir):
    for item_id, details in inventory.items():
        # Create the QR code content
        qr_content = (
            f"ID: {item_id}\n"
            f"Name: {details['name']}\n"
            f"Quantity: {details['quantity']}\n"
            f"Location: {details['location']}"
        )

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_content)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image
        file_name = f"{item_id}.png"
        file_path = os.path.join(output_dir, file_name)
        qr_image.save(file_path)
        print(f"Saved QR Code for {item_id} as {file_path}")

# Generate QR codes
generate_qr_codes(inventory, output_dir)
