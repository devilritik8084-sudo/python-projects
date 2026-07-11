import requests
from datetime import datetime

API_KEY = "833bba515455f64f8003b33169a4c04f"

while True:

    print("\n========== WEATHER APP ==========")
    print("1. Current Weather")
    print("2. 5-Day Forecast")
    print("3. View Weather History")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        city = input("Enter City Name: ")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:

            sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset = datetime.fromtimestamp(data["sys"]["sunset"])

            print("\n========== CURRENT WEATHER ==========")
            print("City        :", data["name"])
            print("Country     :", data["sys"]["country"])
            print("Temperature :", data["main"]["temp"], "°C")
            print("Feels Like  :", data["main"]["feels_like"], "°C")
            print("Humidity    :", data["main"]["humidity"], "%")
            print("Pressure    :", data["main"]["pressure"], "hPa")
            print("Visibility  :", data["visibility"], "meters")
            print("Weather     :", data["weather"][0]["description"])
            print("Wind Speed  :", data["wind"]["speed"], "m/s")
            print("Sunrise     :", sunrise.strftime("%I:%M %p"))
            print("Sunset      :", sunset.strftime("%I:%M %p"))

            with open("weather_history.txt", "a") as file:
                file.write(
                    f"{datetime.now()} | "
                    f"{data['name']} | "
                    f"{data['main']['temp']}°C | "
                    f"{data['weather'][0]['description']}\n"
                )

        else:
            print("Error:", data.get("message"))

    elif choice == "2":

        city = input("Enter City Name: ")

        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data["cod"] == "200":

            print("\n======= 5-DAY FORECAST =======")

            for item in data["list"][::8]:
                print("----------------------------")
                print("Date :", item["dt_txt"])
                print("Temp :", item["main"]["temp"], "°C")
                print("Weather :", item["weather"][0]["description"])

        else:
            print("Error:", data.get("message"))

    elif choice == "3":

        try:
            with open("weather_history.txt", "r") as file:
                print("\n======= WEATHER HISTORY =======")
                print(file.read())
        except FileNotFoundError:
            print("No History Found.")

    elif choice == "4":

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")