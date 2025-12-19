import requests
import pandas as pd

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        if request.method == 'POST':
            base_url="http://api.weatherstack.com/current"
            key=open('personal.txt','r').read()
            city=request.form.get('city')

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
        except KeyError:
            print("Error retrieving data:", data.get("error", "Unknown error"))

        except Exception as e:
            print("An unexpected error occurred:", str(e))
        return render_template('index.html', weather=weather_data)
    else:
        return render_template('index.html', weather=None)
if __name__ == '__main__':
    app.run(debug=True)