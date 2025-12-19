import requests
import pandas as pd

base_url="http://api.weatherstack.com/current"
key=open('personal.txt','r').read()
city="Wote"

url=f"{base_url}?access_key={key}&query={city}"

responce=requests.get(url)
data=responce.json()

try:
    weather_data = {
        "Country": [data['location']['country']],
        "City": [data['location']['name']],
        "Region": [data['location']['region']],
        "Temperature": [data['current']['temperature']],
        "sunrise": [data['astro']['sunrise']] if 'astro' in data else ['N/A'],
        "sunset": [data['astro']['sunset']] if 'astro' in data else ['N/A'],
        "Moon phase": [data['astro']['moon_phase']] if 'astro' in data else ['N/A'],
        "Wind speed": [data['current']['wind_speed']],
        "wind degree": [data['current']['wind_degree']],
        "wind direction": [data['current']['wind_dir']],
        "cloudcover": [data['current']['cloudcover']]
    }

    df = pd.DataFrame(weather_data)
    print(df)
except KeyError:
    print("Error retrieving data:", data.get("error", "Unknown error"))

except Exception as e:
    print("An unexpected error occurred:", str(e))