import requests
from pprint import pprint
import os
import datetime

key = os.environ.get('FORECAST_KEY')
url = f'https://api.openweathermap.org/data/2.5/forecast?'

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('Sorry, could not get weather')
    else:
        current_temp, weather_description, wind_speed, time_stamp = get_forecast(weather_data)
        title_message = f"\n\n\n\t\tWeather Forecast {location.upper()}"
        print(title_message)
        for temp, description, wind, time in zip(current_temp, weather_description, wind_speed, time_stamp): # simultaneously runs different for loops at the same time
            print(f"{time} | {'{:.1f}'.format(temp)} F | {description:<16} | {wind:<6}MPH")

def get_location():
    city, country = '',''
    while len(city) == 0:
        city = input('Enter the city: ')
    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ')
    location = f'{city},{country}'
    return location

def get_current_weather(location, key):
    try:
        query = {'q': location, 'units': 'imperial', 'appid':key}
        response = requests.get(url, params = query)
        response.raise_for_status() # Raise exception for 400 or 500 errors
        data = response.json() # this may error too, if response is not JSON
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text) # added for debugging
        return None, ex

def get_forecast(weather_data):
    "Takes data from api response and converts it into usable data."
    try:
        temp = []
        weather_description = []
        wind_speed = []
        time_stamp = []
        for info in weather_data['list']:
            temp.append(info['main']['temp'])
            weather_description.append(info['weather'][0]['description'])
            wind_speed.append(info['wind']['speed'])
            time_stamp.append(info['dt_txt'])
        return temp, weather_description, wind_speed, time_stamp
    except KeyError:
        print('This data is not in the format expected')
        return 'Unknown'

if __name__ == '__main__':
    main()