import requests

# step 1: Define API endpoint and parameters
api_url = "https://api.example.com/weather"
api_key = "the_api_key"
city = "Dellys"

# step 2: make request to API
response = requests.get(api_url, params={"city":city, "apiKey":api_key})

# step 3: check if api request is successful ( status code 200)
if response.status_code == 200:
    
    # step 4: parse the data into json format
    data = response.json()
    temperature = data["temperature"]
    weather_description = data["description"]
    
    # step 5: use the data
    print(f"the current temperature in {city} is {temperature}°C. {weather_description}.")
    
#step 6: handle error
else:
    print("Failed to fetch weather data.")
