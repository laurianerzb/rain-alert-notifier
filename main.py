import requests
from twilio.rest import Client
import os

# twilio credentials
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
# open weather credentials
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_SECRET = os.environ.get("OPEN_WM_API_KEY")

parameters = {
    'lat': 39.1422,
    'lon': 117.1767,
    'appid': API_SECRET,
    'exclude': 'current, minutely, daily'
}
response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
data_weather = data['list'][:12]
will_rain = False
for hour_data in data_weather:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token,)
    message = client.messages \
        .create(
            body="It's going to rain today ☔",
            from_='YOUR_VIRTUAL_PHONE_NUMBER',
            to='YOUR_VERIFIED_PHONE_NUMBER'
        )
    print(message.status)
