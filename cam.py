import firebase_admin
from firebase_admin import credentials, storage
from picamera import PiCamera
import time


# Replace 'path/to/your/credentials.json' with the path to your Firebase credentials JSON file
cred = credentials.Certificate('path/to/your/credentials.json')
firebase_admin.initialize_app(cred)

# Initialize Storage
storage_client = storage.Client()


camera = PiCamera()

while True:
    # Capture image
    image_path = 'image.jpg'
    camera.capture(image_path)

    # Upload image to Firebase Storage
    bucket = storage_client.get_bucket('your_storage_bucket')  # Replace with your storage bucket name
    blob = bucket.blob('images/' + image_path)
    blob.upload_from_filename(image_path)

    # Get the public URL of the uploaded image
    image_url = blob.public_url

    # Process the image URL as needed

    time.sleep(5)  # Adjust the interval as needed
