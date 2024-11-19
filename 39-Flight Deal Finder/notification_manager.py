import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv('TW_SID'), os.getenv("TW_TOKEN"))

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.getenv("TW_NUMBER"),
            body=message_body,
            to=os.getenv("MY_NUMBER")
        )
        # Prints if successfully sent.
        print(message.sid)

    # def send_whatsapp(self, message_body):
    #     message = self.client.messages.create(
    #         from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
    #         body=message_body,
    #         to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
    #     )
    #     print(message.sid)