from twilio.rest import Client
#Recovery code:  4DX-rtE8MYuIr92n4kPHciHRkWXDkz_4q9Mcs3Xd
TWILIO_SID = "Twilio SID"
TWILIO_AUTH_TOKEN = "Authentification Token"
TWILIO_VIRTUAL_NUMBER = "Twilo Virtual Number"
TWILIO_VERIFIED_NUMBER = "Verified Personal/User Number"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
