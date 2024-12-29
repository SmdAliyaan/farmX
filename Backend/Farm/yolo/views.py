from django.shortcuts import render, get_object_or_404
from ultralytics import YOLO
import cv2
from Inv_management.models import Product
from twilio.rest import Client


def send_report_via_sms(qty):
    # Twilio client setup (replace with your Twilio credentials)
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)

    message = f"Banana stock updated: {qty} remaining."
    try:
        client.messages.create(
            body=message,
            from_="your_twilio_number",
            to="receiver_phone_number"
        )
        print("SMS sent successfully.")
    except Exception as e:
        print(f"Failed to send SMS: {e}")


def out_of_stock(request):
    if request.method == 'GET':
        # Initialize YOLO model
        model = YOLO('yolov8n.pt')

        # Retrieve the product by its name "Banana"
        banana_product = get_object_or_404(Product, name="Banana")

        # Check if bananas are in stock
        if banana_product.quantity_remaining > 0:
            # Decrease the quantity of bananas by 1
            banana_product.quantity_remaining -= 1
            qty = banana_product.quantity_remaining

            # Send SMS report
            send_report_via_sms(qty)

            banana_product.save()
            message = "Banana quantity decreased successfully."
        else:
            message = "No bananas left in stock."

        print(message)

        # Open video capture device
        cap = cv2.VideoCapture(0)  # Use appropriate video capture device

        while cap.isOpened():
            # Read frame from video capture device
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            # Perform object detection on the frame
            results = model(frame, show=True)

            # Wait for key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # Break the loop if 'q' key is pressed

        # Release video capture device and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

        # Render the result on a webpage
        return render(request, 'out_of_stock.html', {'message': message})
    
    else:
        return render(request, 'out_of_stock.html')

# Create your views here.
