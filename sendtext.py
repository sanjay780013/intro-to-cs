from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC53b4fcc575f3ac27f0ecfa79f05e5347"
# Your Auth Token from twilio.com/console
auth_token  = "27e31956e9717077f10b001e3ac8ba85"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12182099036", 
    from_="+12182107825",
    body="K cha ho kafle sherey!")

print(message.sid)
