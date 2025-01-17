import requests

api_key = "5d32c1bcf0a08f33b31fe58e53ccc7d6"

user_input = input("Enter a city: ")
user_input.title()

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:

    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humid = weather_data.json()['main']['humidity']

    tempCelsius = round((temp-32) * 5/9)
    degree_sign = u'\N{DEGREE SIGN}'


    print(f"\nThe weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {tempCelsius}{degree_sign} Celsius")
    print(f"The humidity in {user_input} is: {humid}%")

