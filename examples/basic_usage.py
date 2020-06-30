import os

from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')


def example():
    """
    Some example usage of different twilio resources.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    print('Sending a message...')
    new_message = client.messages.create(to='XXXX', from_='YYYY', body='Free yourself with Twexit!')
    print(new_message)


if __name__ == '__main__':
    example()
