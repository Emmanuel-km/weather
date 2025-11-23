from flask import Flask, render_template, request, jsonify, send_file
import requests
import json
import os
from datetime import datetime, timedelta
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

# Make sure the images directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Mock API keys (replace with actual keys in production)
WEATHER_API_KEY = "33690e6bdef33da03573c64f37326086"
GEMINI_API_KEY = "AIzaSyBRoo0V0edF992VD5UVhW2M3lqNoGaLrAQ"

@app.route('/')
def index():
    return render_template('index.html')


def generate_energy_analysis(current_weather, historical_weather, location):
    # In a real application, you would call the Gemini API here
    # For this demo, we'll return mock analysis
    
    solar_potential = current_weather['solar_radiation'] * 0.15  # Simple calculation
    wind_potential = current_weather['wind_speed'] * 0.8  # Simple calculation
    
    analysis = {
        'solar_potential': f"{solar_potential:.2f} kWh/m²/day",
        'wind_potential': f"{wind_potential:.2f} kWh/day for a standard turbine",
        'temperature_change': f"{current_weather['temperature'] - historical_weather['temperature']:.1f}°C increase over 30 years",
        'recommendations': [
            "High solar potential - consider installing photovoltaic panels",
            "Moderate wind potential - small wind turbines could supplement energy needs",
            "Implement energy storage systems to maximize renewable utilization"
        ],
        'grid_integration': "Good conditions for connecting renewable sources to the electrical grid"
    }
    
    return analysis

def generate_visualization(current_weather, historical_weather, energy_analysis, location):
    # Create a comparison chart
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # Temperature comparison
    temperatures = [historical_weather['temperature'], current_weather['temperature']]
    years = ['30 Years Ago', 'Current']
    ax1.bar(years, temperatures, color=['lightblue', 'orange'])
    ax1.set_title(f'Temperature Comparison in {location}')
    ax1.set_ylabel('Temperature (°C)')
    
    # Solar radiation comparison
    solar_rad = [historical_weather['solar_radiation'], current_weather['solar_radiation']]
    ax2.bar(years, solar_rad, color=['lightgreen', 'green'])
    ax2.set_title('Solar Radiation Comparison')
    ax2.set_ylabel('Solar Radiation (W/m²)')
    
    # Wind speed comparison
    wind_speeds = [historical_weather['wind_speed'], current_weather['wind_speed']]
    ax3.bar(years, wind_speeds, color=['lightgray', 'blue'])
    ax3.set_title('Wind Speed Comparison')
    ax3.set_ylabel('Wind Speed (km/h)')
    
    # Energy potential
    solar_potential = current_weather['solar_radiation'] * 0.15
    wind_potential = current_weather['wind_speed'] * 0.8
    energy_sources = ['Solar', 'Wind']
    energy_potentials = [solar_potential, wind_potential]
    ax4.bar(energy_sources, energy_potentials, color=['yellow', 'cyan'])
    ax4.set_title('Renewable Energy Potential')
    ax4.set_ylabel('Energy (kWh)')
    
    plt.tight_layout()
    
    # Save the plot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"weather_analysis_{timestamp}.png"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    plt.savefig(filepath)
    plt.close()
    
    return filename

if __name__ == '__main__':
    app.run(debug=True)