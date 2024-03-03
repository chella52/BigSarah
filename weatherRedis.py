# All NESCESSARY IMPORTS
import requests
import json
import redis

# FETCHING WEATHER DATA USING THE API URL
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=e68dca61b59308e6452d99b454269718"
    try:
        response = requests.get(url)
        response.raise_for_status() # THIS RAISES AN EXCEPTION FOR BAD STATUS CODES
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data for", city, ":", e)
        return None
# STORING WEATHER DATA INTO REDIS 
def insert_weather_data_into_redis(redis_client, weather_data):
    for city, data in weather_data.items():
        redis_client.set(city, json.dumps(data))

def main():
    # LISTING THE CITIES THAT I WANTED TO FETCH FROM THE WEATHER API (20 RECORDS)
    cities = [
        "London", "New York", "Tokyo", "Paris", "Sydney",
        "Berlin", "Moscow", "Dubai", "Singapore", "Toronto",
        "Los Angeles", "Seoul", "Rome", "Mumbai", "Beijing",
        "Bangkok", "Istanbul", "Rio de Janeiro", "Cairo", "Amsterdam"
    ]
    # UNIQUE API KEY GENERATED FOR EACH USER
    api_key = input("Enter your OpenWeatherMap API key: e68dca61b59308e6452d99b454269718")

    # TO INITIALIZE THE REDIS_CLI 
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    # WEATHER DATA OF ALL THE CITIES IS STORED IN A DICTIONARY
    weather_data_all = {}

    # FETCHING WEATHER DATA OF EACH CITY AND STORING IT IN THE DICTIONARY 
    for city in cities:
        weather_data = fetch_weather_data(city, api_key)
        if weather_data:
            weather_data_all[city] = weather_data
        else:
            print(f"Failed to fetch weather data for {city}.")

    # INSERTING THE WEATHER DATA INTO REDIS
    insert_weather_data_into_redis(redis_client, weather_data_all)
    # PRINTING THE WEATHER DATA
    print("Weather data inserted into Redis.")

if __name__ == "__main__":
    main()
