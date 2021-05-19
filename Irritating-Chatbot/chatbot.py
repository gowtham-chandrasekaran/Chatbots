from twilio.rest import Client

account_sid = 'Your account sid'
auth_token = 'Your auth token'
client = Client(account_sid, auth_token)


def irritating_message():
    message = client.messages.create(
            from_='whatsapp:your twilio number',
            body='Idiot',
            to='whatsapp:then number you want to send messages to'
        )

    print(message.sid)
