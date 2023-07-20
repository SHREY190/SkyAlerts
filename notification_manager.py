from twilio.rest import Client
#Recovery code:  4DX-rtE8MYuIr92n4kPHciHRkWXDkz_4q9Mcs3Xd
TWILIO_SID = "AC738009c86866ce9a48f8373776fa6c01"
TWILIO_AUTH_TOKEN = "4847585f3360398f51c1641b7af764b6"
TWILIO_VIRTUAL_NUMBER = "+14027714219"
TWILIO_VERIFIED_NUMBER = "+918770080485"

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