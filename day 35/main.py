import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?&appid"
OWM_API_KEY = "04504a1938ffdb3d3aac4fcbd978f355"
account_sid = "ACe5cbe109012c61b79a4d0ea9b7ce47f3"
auth_token = "6b06582e920f3505beef8e17285ca47c"

parameters = {
    "lat": 51.4714925,
    "lon": -0.3346952,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_twelve_hours = weather_data["hourly"][:12]

will_rain = False
for hours in weather_twelve_hours:
    condition_code = hours["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="+19087749763",
            to="+447475309579",
        )

    print(message.sid)
