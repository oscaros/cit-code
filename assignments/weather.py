from urllib.error import HTTPError
import requests

url = "http://api.openweathermap.org/data/2.5/weather?"
open_weather_api_key = "672d716a8e01ce7958de00be9a78cd8f"

#weather func
def weather():
    input_city = input('Enter city name: \n')
   
    try:
        req=requests.get(url  + "appid=" + open_weather_api_key + "&q=" + input_city)
        result = req.json()
        print(result)

    except HTTPError:
        print("Error {}".format(HTTPError))
    #return weather

#main func
def main():
   weather()

if __name__ == '__main__':
    main()
