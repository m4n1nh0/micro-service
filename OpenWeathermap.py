import json

import requests

key = "SUA_LICENCA"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
url_cord = "https://api.openweathermap.org/data/2.5/onecall?"


def weather_city(city):
    url = base_url + "appid=" + key + "&q=" + city
    response = requests.get(url)
    ret_json = response.json()
    temp = 0.0
    if ret_json["cod"] != "404":
        obj_json = ret_json["main"]
        temp = (273.15 - obj_json["temp"]) * -1
    return temp


def weather_cord(lat, lon):
    url = url_cord + "appid=" + key + "&lat=" + str(lat) + "&lon=" + str(lon)
    response = requests.get(url)
    ret_json = json.loads(response.text)
    obj_json = ret_json["current"]
    temp = (273.15 - obj_json["temp"]) * -1
    return temp
