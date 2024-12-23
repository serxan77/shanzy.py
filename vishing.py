from twilio.rest import Client

def send_vishing_call(phone_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=phone_number,
        from_="your_twilio_number",
        url="http://demo.twilio.com/docs/voice.xml"
    )

    print(call.sid)

# İstifadə:
send_vishing_call("+1234567890", "Bu sizin bankinizdan zəngdir, zəhmət olmasa məlumatlarinizi təqdim edin.")
