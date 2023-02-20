import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# api key from .env file to hide it
api_key = os.getenv("API_KEY")

# setting up params that will be a part of the response url below
weather_params = {
    "lat": 37.028271,
    "lon": -76.342339,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

my_email = "pythontestberry@gmail.com"
# password from app generator on gmail
password = os.getenv("PASSWORD")
other_email = "berrypythontest@yahoo.com"

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()

# slicing the data to get only the first 12 hours
weather_slice = weather_data["hourly"][:12]

# establishing a true/false variable so if the variable is true then it will print the statement only once because it's
# outside the loop
is_rain = False

# iterating over each hour to 12 then narrowing the data down to get the weather id to see if it is less than 700
for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]['id']
    if int(weather_id) < 700:
        is_rain = True

if is_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # start transport layer security to secure the connection to the email server
        connection.starttls()
        # login process
        connection.login(user=my_email, password=password)
        # sending the email from one address to the other with message...adding subject and /n to make
        # sure it doesn't go into spam box
        connection.sendmail(from_addr=my_email, to_addrs=other_email,
                            msg=f"Subject:Look Up!\n\nBring an Umbrella!")



