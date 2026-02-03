import requests
import os
from dotenv import load_dotenv
if not API_Key:
    print("Error: API Key nahi mili! Pehle .env file setup karein.")
    exit()

# .env (file se data load karne ke liye)
load_dotenv()

# user se city ka name puchna
city_name = input("Enter city name: ")
API_Key = os.getenv('OPENWEATHER_API_KEY')

# 2. URL
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Data extract karna
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Formatting ke saath print karna
        print("-" * 30)
        print(f" Weather in {city_name.upper()}")
        print("-" * 30)
        print(f" Condition   : {desc.capitalize()}")
        print(f" Temperature : {temp}°C (Feels like {feels_like}°C)")
        print(f" Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind_speed} m/s")
        print("-" * 30)
        
    elif response.status_code == 404:
        print(f"Error: City '{city_name}' nahi mili. Spelling check karein!")
        print("('Eske aas-paas ke city ka name daal kar try kro...!!')")
    else:
        print(f" Error: {response.status_code}")
        print(response.json().get('message'))

except Exception as e:
    print(f"Kuch galat hua: {e}")

    
    