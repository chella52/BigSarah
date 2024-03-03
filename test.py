import requests

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=e68dca61b59308e6452d99b454269718"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data for", city, ":", e)
        return None

def main():
    # List of cities for which you want to fetch weather data
    cities = [
        "London", "New York", "Tokyo", "Paris", "Sydney",
        "Berlin", "Moscow", "Dubai", "Singapore", "Toronto",
        "Los Angeles", "Seoul", "Rome", "Mumbai", "Beijing",
        "Bangkok", "Istanbul", "Rio de Janeiro", "Cairo", "Amsterdam"
    ]
    api_key = input("Enter your OpenWeatherMap API key: ")
    
    # Dictionary to store weather data for each city
    weather_data_all = {}
    
    # Fetch weather data for each city and store it in the dictionary
    for city in cities:
        weather_data = fetch_weather_data(city, api_key)
        if weather_data:
            weather_data_all[city] = weather_data
        else:
            print(f"Failed to fetch weather data for {city}.")
    
    # Print all the weather data
    for city, data in weather_data_all.items():
        print(f"Weather data for {city}:")
        print(data)

if __name__ == "__main__":
    main()
