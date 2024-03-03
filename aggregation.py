# ALL NECESSARY IMPORTS
import requests
import json

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=e68dca61b59308e6452d99b454269718"
    try:
        response = requests.get(url)
        response.raise_for_status()  # RAISES AN EXCEPTION FOR BAD STATUS CODES
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data for", city, ":", e)
        return None

def main():
    # LIST OF CITIES I WANT TO FETCH WEATHER DATA FROM
    cities = ["Berlin", "Moscow", "Dubai", "Singapore", "Toronto"]
    api_key = "e68dca61b59308e6452d99b454269718"

    # FETCHING WEATHER DATA FOR EACH CITY
    city_data_all = {}
    for city in cities:
        city_data = fetch_weather_data(city, api_key)
        if city_data:
            city_data_all[city] = city_data
        else:
            print(f"Failed to fetch weather data for {city}.")

    # STANDARD TEMPERATURE CONVERSION FOR EACH CITY 
    temperatures = [city_data['main']['temp'] - 273.15 for city, city_data in city_data_all.items()]

    # CALCULATING AVERAGE TEMPERATURE
    average_temperature = sum(temperatures) / len(temperatures)
    
    # PRINTING AVERAGE TEMPERATURE
    print("Average Temperature:", round(average_temperature, 2), "°C")

if __name__ == "__main__":
    main()
