import requests
import matplotlib.pyplot as plt

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=e68dca61b59308e6452d99b454269718"
    try:
        response = requests.get(url)
        response.raise_for_status()   # RAISES AN EXCEPTION FOR BAD STATUS CODES
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data for", city, ":", e)
        return None

def main():
   # LIST OF CITIES I WANT TO FETCH WEATHER DATA FROM
    cities = ["London", "New York", "Tokyo", "Paris", "Sydney",
              "Berlin", "Moscow", "Dubai", "Singapore", "Toronto",
              "Los Angeles", "Seoul", "Rome", "Mumbai", "Beijing",
              "Bangkok", "Istanbul", "Rio de Janeiro", "Cairo", "Amsterdam"]
    
    api_key = "e68dca61b59308e6452d99b454269718"

    # FETCHING WEATHER DATA FOR EACH CITY
    city_data_all = {}
    for city in cities:
        city_data = fetch_weather_data(city, api_key)
        if city_data:
            city_data_all[city] = city_data
        else:
            print(f"Failed to fetch weather data for {city}.")

    # EXTRACTING LATITUDE AND LONGITUDE FOR EACH CITY
    latitudes = []
    longitudes = []
    for city, data in city_data_all.items():
        latitudes.append(data['coord']['lat'])
        longitudes.append(data['coord']['lon'])

    # PLOTTING SCATTERPLOT
    plt.figure(figsize=(10, 6))
    plt.scatter(longitudes, latitudes, c='red', s=100, alpha=0.5)
    plt.title("Scatterplot of Cities")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
