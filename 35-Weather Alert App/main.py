# -------------------- MODULES --------------------
"""imported requests module"""
import requests

"""imported Client class from the twilio.rest module"""
from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()
import os


# -------------------- API AND LOCATION DATA --------------------
"""openweather api endpoint"""
owEp = "https://api.openweathermap.org/data/2.5/weather"

"""openweather api key"""
owApiKey = os.getenv('OW_API_KEY')

"""location data"""
MY_LAT = os.getenv('LAT')
MY_LONG = os.getenv('LON')

"""dictionary to hold the parameters"""
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": owApiKey,
    "exclude": "current,minutely,daily"
}


# -------------------- GETTING DATA FROM OPENWEATHER--------------------
"""variable to store the response"""
response = requests.get(url=owEp, params=parameters)
response.raise_for_status()

"""variable to store the condition of weather"""
weatherCondition = ''
weather_messages = {
    "thunderstorm": "🌩️It might thunderstorm today! Stay safe and indoors if possible.",
    "drizzle": "🌧️There's some light rain or drizzle today. Bring an umbrella if you’re heading out!",
    "rain": "☔️Expect rain today! Stay dry and plan accordingly.",
    "snow": "❄️Snow is expected today. Dress warmly and take care while traveling.",
    "clear": "☀️The sky is clear today! Enjoy the beautiful weather.",
    "clouds": "🌥️It's a cloudy day. Perfect weather for a cozy indoor activity.",
    "mist": "🌫️There’s mist today. Drive carefully if you’re on the road."
}

weatherId = response.json()['weather'][0]['id']
# print(weatherId)
def get_message_for_weather(weather_id):
    """returns an appropriate message based on the weather ID."""
    if 200 <= weather_id < 300:
        return weather_messages["thunderstorm"]
    elif 300 <= weather_id < 400:
        return weather_messages["drizzle"]
    elif 500 <= weather_id < 600:
        return weather_messages["rain"]
    elif 600 <= weather_id < 700:
        return weather_messages["snow"]
    elif weather_id == 800:
        return weather_messages["clear"]
    elif 801 <= weather_id < 900:
        return weather_messages["clouds"]
    elif 700 <= weather_id < 800:
        return weather_messages["mist"]
    else:
        return "Weather is unusual today. Stay prepared!"


# -------------------- WORKING WITH TWILIO --------------------
"""twilio sid"""
twAccountSid = os.getenv('TW_ACCOUNT_SID')

"""twilio token"""
twAuthToken = os.getenv('TW_AUTH_TOKEN')
"""setting up twilio client"""
client = Client(twAccountSid, twAuthToken)

"""message will be sent when, if willRain holds true"""
message = client.messages.create(
  body=get_message_for_weather(weatherId),
  from_=os.getenv('TW_PHONE_NUMBER'),
  to=os.getenv('MY_PHONE_NUMBER')
)
print(message.status)