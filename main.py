from fastapi import FastAPI
from pydantic import BaseModel

import OpenWeathermap
import Spotfyapi

app = FastAPI()
Weathermap = OpenWeathermap
Playlist = Spotfyapi


class Retorno(BaseModel):
    info: str
    temp: float
    playlist: str


@app.get("/")
async def root():
    return {"message": "Bem vindo(a)"}


@app.get("/city/{city}")
async def put_City(city: str):
    temp = Weathermap.weather_city(city)
    url = Playlist.playlist(temp)
    return {
        "Info": city,
        "Temp": '{0:.2f}'.format(temp),
        "url": url,
    }


@app.get("/Cord/{lat}&{lon}")
async def put_Cord(lat: float, lon: float):
    temp = Weathermap.weather_cord(lat, lon)
    url = Playlist.playlist(temp)
    return {
        "Info": "cord" + str(lat) + "/" + str(lon),
        "Temp": '{0:.2f}'.format(temp),
        "url": url,
    }
