from geopy.geocoders import Nominatim

# 위치와 관련된 모듈

geolocator = Nominatim(user_agent="songyi")
location = geolocator.geocode("Seoul, South Korea")
print(location)
print((location.latitude, location.longitude))
print(location.raw)

# 실생활 project (문자보내기)

  
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = 'AC98c0977c5dbdb9923bec6a38072cf3f4'
auth_token = '8b5a1664b2a180e75bf56286cbfe8dfb'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+821032991099",
    from_="+13345092800",
    body="Hello there!")