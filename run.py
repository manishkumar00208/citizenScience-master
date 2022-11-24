from twilio.rest import Client

account_sid = 'AC3870e9de6dda09a9989d89f0a00c67e3'
auth_token = '0e328f21ca61dd6c0f6cd847c7bc94b0'
client = Client(account_sid, auth_token)

message = client.messages.create(to='+919133288288')

print(message.sid)