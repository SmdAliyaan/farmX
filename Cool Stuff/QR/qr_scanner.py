import os
from PIL import Image
import pyzbar.pyzbar as pyzbar

# Folder containing QR codes
qr_folder = "qr_codes"
os.chdir(".\QR")

def scan_qr_code(image_path):
    """
    Scans a QR code from the given image path and returns the decoded content.
    """
    try:
        img = Image.open(image_path)
        decoded_objects = pyzbar.decode(img)
        if decoded_objects:
            for obj in decoded_objects:
                print(f"Decoded content from {image_path}:")
                print(obj.data.decode("utf-8"))
        else:
            print(f"No QR code found in {image_path}")
    except Exception as e:
        print(f"Error scanning {image_path}: {e}")

def scan_all_qr_codes(folder):
    """
    Scans all QR codes in the specified folder.
    """
    if not os.path.exists(folder):
        print(f"Folder '{folder}' does not exist.")
        return

    files = os.listdir(folder)
    qr_files = [f for f in files if f.endswith(".png") or f.endswith(".jpg")]

    if not qr_files:
        print(f"No QR code images found in '{folder}'.")
        return

    for qr_file in qr_files:
        image_path = os.path.join(folder, qr_file)
        scan_qr_code(image_path)

# Run the program
print(f"Scanning QR codes from '{qr_folder}'...")
scan_all_qr_codes(qr_folder)
