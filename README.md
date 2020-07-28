# Telnyx "Twexit" Python Library

The Telnyx "Twexit" Python library allows users to send messages and validate webhooks with minimal changes to their existing Twilio messaging code.

## Installation

This SDK can be installed either via `pip`:

```
pip install twexit
```

or direct from source by downloading and unzipping the repository from here, then from within the `twexit-python` folder, run
```
python setup.py install
```


## Account Setup

1. Complete the [Portal Setup](https://developers.telnyx.com/docs/v2/messaging/quickstarts/portal-setup) to set up a messaging-enabled number.

1. Follow the additional [Twexit setup steps](https://developers.telnyx.com/docs/v2/messaging/twexit) to configure webhooks

## Usage

### Send a message

```py
from twilio.rest import Client

# Your organization ID from
account_sid = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
# An API key from https://portal.telnyx.com/#/app/api-keys
auth_token = "KEY0123456789xxxxx"

message = client.messages.create(
    to="+13125550123",
    from_="+16165550123",
    body="Free yourself with Twexit!"
)

print(message.sid)
```

## Webhook Validation

Twexit uses a fast asymmetric signing algorithm, Ed25519, to avoid issues discovered with SHA-1. To switch from the HMAC-SHA1 signing method, follow these steps:

1. Obtain your account's public key at https://portal.telnyx.com/#/app/account/public-key

1. Update your application to use the `TwexitRequestValidator` instead of `RequestValidator`

1. Extract the `X-Twexit-Signature` from the request and provide that when calling the validator.

```py
from twilio.request_validator import TwexitRequestValidator

public_key = "abcdef123456xxxxx"

validator = TwexitRequestValidator(public_key)

url = 'https://mycompany.com/myapp.php?foo=1&bar=2'
params = {
    "MessageSid": "CA1234567890ABCDE",
    "ApiVersion": "2010-04-01",
    "Body": "Aloha!",
    "From": "+13125550123",
    "To": "+16165550123",
}

# The X-Twexit-Signature header attached to the request
twexit_signature = '0/KCTR6DLpKmkAf8muzZqo1nDgQ='

print(validator.validate(url, params, twexit_signature))
```

## Caveats

This SDK currently only provides the capability to send messages via REST and validate webhooks when receiving messages. Configuration of the messaging product and other products (voice, fax) are not yet supported.
