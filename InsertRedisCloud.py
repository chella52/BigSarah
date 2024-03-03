# ALL NECESSARY IMPORTS 
import requests
import json
import redis
# FETCHING WEATHER DATA USING URL
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
# STORING THE WEATHER DATA INTO REDIS CLIENT
def insert_weather_data_into_redis(redis_client, weather_data):
    for city, data in weather_data.items():
        redis_client.set(city, json.dumps(data))

def main():
    # LIST OF CITIES I WANT TO FETCH WEATHER DATA FROM
    cities = [
        "London", "New York", "Tokyo", "Paris", "Sydney",
        "Berlin", "Moscow", "Dubai", "Singapore", "Toronto",
        "Los Angeles", "Seoul", "Rome", "Mumbai", "Beijing",
        "Bangkok", "Istanbul", "Rio de Janeiro", "Cairo", "Amsterdam"
    ]
    api_key = input("Enter your OpenWeatherMap API key: e68dca61b59308e6452d99b454269718")

    # INITIALIZING REDIS CLIENT WITH REDIS CLOUD CONNECTION DETAILS 
    redis_host = "redis-10003.c274.us-east-1-3.ec2.cloud.redislabs.com"
    redis_port = 10003  
    redis_password = "kPZGh7mDzdbF7iXBI3xWbFmhEX7qJB7z"
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    # DICTIONARY TO STORE WEATHER DATA
    weather_data_all = {}

    # FETCHING EACH CITY'S DATA AND STORING IT IN THE DICTIONARY
    for city in cities:
        weather_data = fetch_weather_data(city, api_key)
        if weather_data:
            weather_data_all[city] = weather_data
            print(f"Weather data for {city}:")
            print(json.dumps(weather_data, indent=4))
        else:
            print(f"Failed to fetch weather data for {city}.")

    # INSERT WEATHER DATA INTO REDIS
    insert_weather_data_into_redis(redis_client, weather_data_all)
    print("Weather data inserted into Redis.")

if __name__ == "__main__":
    main()
