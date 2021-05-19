from twilio.rest import Client

account_sid = 'AC4830d6b6435b04417f98bf75ba245e07'
auth_token = '4ff90b8a63ebce4857894246bc4046e6'
client = Client(account_sid, auth_token)


def irritating_message():
    message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Idiot',
            to='whatsapp:+919940092534'
        )

    print(message.sid)
