import json
import requests


def convert_F_to_C(degree_in_k):
    degree_in_c = round(degree_in_k - 273.15)
    return degree_in_c


API_key = "4bc5b60fcb39a3e8b945502bda2ff464"
city_name = input("Enter a city name: ")

request = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + API_key

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        weather_description = json_response["weather"][0]["description"]
        print(f"The weather in {city_name} now is {weather_description}.")
        degrees_in_k = json_response["main"]["temp"]
        degrees_in_c = convert_F_to_C(degrees_in_k)
        print(f"The temperature of {city_name} is {degrees_in_c}'C")
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
