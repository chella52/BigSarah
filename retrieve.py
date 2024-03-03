import redis
import json

#CONECTING TO REDIS
r = redis.Redis(host='localhost', port=6379, db=0)

# RETRIEVE JSON DATA FROM REDIS
json_string = r.get('weather_data')

# CHECK IF THE DATA IS RETRIEVED
if json_string:
    # DECODE JSON STRING INTO PYTHON DICTIONARY
    json_data = json.loads(json_string)

    print("City name:", json_data["name"])
    print("Temperature:", json_data["main"]["temp"])
    print("Description:", json_data["weather"][0]["description"])
    print("JSON data parsed successfully from Redis.")
else:
    print("No data found in Redis.")
