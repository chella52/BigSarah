# ALL NECESSARY IMPORTS
import requests
import json
import matplotlib.pyplot as plt

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=e68dca61b59308e6452d99b454269718"
    try:
        response = requests.get(url)
        response.raise_for_status()  #  RAISES AN EXCEPTION FOR BAD STATUS CODES
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data for", city, ":", e)
        return None

def main():
    # LIST OF CITIES I WANT TO FETCH WEATHER DATA FROM
    cities = ["Berlin", "Paris", "Sydney"]
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

    # PLOTTING BAR PLOT
    plt.figure(figsize=(10, 6))
    plt.bar(city_data_all.keys(), temperatures, color=['blue', 'green', 'orange'])
    plt.title("Temperature in Berlin, Paris, and Sydney")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.grid(axis='y')
    plt.show()

if __name__ == "__main__":
    main()
