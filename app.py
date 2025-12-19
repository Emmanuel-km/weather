import requests
import pandas as pd

base_url="http://api.weatherstack.com/current"
key=open('personal.txt','r').read()
city="Wote"

url=f"{base_url}?access_key={key}&query={city}"

responce=requests.get(url)
data=responce.json()
#data=pd.DataFrame(data)

print(data)