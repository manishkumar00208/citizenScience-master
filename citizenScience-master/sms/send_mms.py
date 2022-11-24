from twilio.rest import Client
import os

account_sid = os.environ["AC3870e9de6dda09a9989d89f0a00c67e3"]
auth_token = os.environ["0e328f21ca61dd6c0f6cd847c7bc94b0"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919133288288",
    from_="+1 970 645 8942",
    body="This is the ship that made the Kessel Run in fourteen parsecs?",
    media_url=["https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg"])

print(message.sid)
print(message.status)
print(message.media._uri)