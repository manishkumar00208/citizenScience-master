from twilio.rest import Client
import os

account_sid = os.environ['AC3870e9de6dda09a9989d89f0a00c67e3']
auth_token = os.environ['0e328f21ca61dd6c0f6cd847c7bc94b0']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919133288288",
    from_="+19706458942",
    body="Hello from Python!")

"""
multiple numbers

numbers_to_message = ['+15558675310', '+14158141829', '+15017122661']
for number in numbers_to_message:
    client.messages.create(
        body = 'Hello from my Twilio number!',
        from_ = '+17174475615',
        to = 'number'
    )
"""

print(message.sid)
print(message.status)