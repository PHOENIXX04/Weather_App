import requests

API_KEY = "869b67e25b9d98cd89ab3d57c27178b9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        print(f"Weather in {city}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Condition: {weather_data['description']}")
    else:
        print(f"City {city} not found.")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
