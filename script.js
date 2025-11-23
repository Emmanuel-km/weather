 document.getElementById('locationForm').addEventListener('submit', function(e) {
e.preventDefault();
            
// Show loading indicator
 document.getElementById('loading').style.display = 'block';
document.getElementById('results').style.display = 'none';
            
// Get form data
const formData = new FormData();
formData.append('country', document.getElementById('country').value);
formData.append('region', document.getElementById('region').value);
 formData.append('area', document.getElementById('area').value);
            
// Send request to server
fetch('/analyze', {
                method: 'POST',
                body: formData
            })
.then(response => response.json())
.then(data => {
                // Hide loading indicator
document.getElementById('loading').style.display = 'none';
                
                // Update current weather
document.getElementById('current-temp').textContent = data.current_weather.temperature + '°C';
                document.getElementById('current-humidity').textContent = data.current_weather.humidity + '%';
                document.getElementById('current-wind').textContent = data.current_weather.wind_speed + ' km/h';
                document.getElementById('current-condition').textContent = data.current_weather.condition;
                
                // Update historical weather
                document.getElementById('historical-temp').textContent = data.historical_weather.temperature + '°C';
                document.getElementById('historical-humidity').textContent = data.historical_weather.humidity + '%';
                document.getElementById('historical-wind').textContent = data.historical_weather.wind_speed + ' km/h';
                document.getElementById('historical-condition').textContent = data.historical_weather.condition;
                
                // Update energy analysis
                document.getElementById('solar-potential').textContent = data.energy_analysis.solar_potential;
                document.getElementById('wind-potential').textContent = data.energy_analysis.wind_potential;
                document.getElementById('temp-change').textContent = data.energy_analysis.temperature_change;
                document.getElementById('grid-integration').textContent = data.energy_analysis.grid_integration;
                
                // Update recommendations
                const recommendationsList = document.getElementById('recommendations');
                recommendationsList.innerHTML = '';
                data.energy_analysis.recommendations.forEach(rec => {
                    const li = document.createElement('li');
                    li.textContent = rec;
                    recommendationsList.appendChild(li);
                });
                
                // Update image
                document.getElementById('analysis-image').src = '/static/images/' + data.image_path;
                
                // Show results
                document.getElementById('results').style.display = 'block';
            })
.catch(error => {
                console.error('Error:', error);
                document.getElementById('loading').style.display = 'none';
                alert('An error occurred while processing your request.');
            });
        });