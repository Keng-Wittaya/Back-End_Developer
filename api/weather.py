import requests

API_key = 'b3d1bec7a9344ee9e9e32964c215136b'
city = 'bangkok'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'

result = requests.get(url).json()
# print(result)
city_name = result['name']
country = result['sys']['country']
weather = result['weather'][0]['main']
description = result['weather'][0]['description']
temp = result['main']['temp'] - 273.15

print(f'เมือง {city_name} ประเทศ {country}')
print(f'สภาพอากาศ {weather} มีลักษณะ {description}')
print(f'อุณหภูมิ {temp} C')