import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

API_KEY = "833bba515455f64f8003b33169a4c04f"

root = tk.Tk()
root.title("🌦 Weather Forecast App")
root.geometry("550x650")

title = tk.Label(
    root,
    text="🌦 Weather Forecast App",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

result = tk.Label(
    root,
    text="Weather information will appear here...",
    font=("Arial", 12),
    justify="left",
    anchor="w",
    width=45,
    height=18,
    relief="groove",
    padx=10,
    pady=10
)
result.pack(pady=15)


def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if str(data.get("cod")) == "200":

        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])

        weather_text = f"""
City           : {data['name']}
Country        : {data['sys']['country']}

Temperature    : {data['main']['temp']} °C
Feels Like     : {data['main']['feels_like']} °C

Humidity       : {data['main']['humidity']} %
Pressure       : {data['main']['pressure']} hPa

Visibility     : {data['visibility']} m

Weather        : {data['weather'][0]['description']}
Wind Speed     : {data['wind']['speed']} m/s

Sunrise        : {sunrise.strftime('%I:%M:%S %p')}
Sunset         : {sunset.strftime('%I:%M:%S %p')}
"""

        result.config(text=weather_text)

        with open("weather_history.txt", "a") as file:
            file.write(
                f"{datetime.now()} | "
                f"{data['name']} | "
                f"{data['main']['temp']}°C | "
                f"{data['weather'][0]['description']}\n"
            )

    else:
        messagebox.showerror("Error", data.get("message"))


def clear_data():
    city_entry.delete(0, tk.END)
    result.config(text="Weather information will appear here...")


def view_history():
    try:
        with open("weather_history.txt", "r") as file:
            history = file.read()

        history_window = tk.Toplevel(root)
        history_window.title("Weather History")
        history_window.geometry("600x400")

        text = tk.Text(history_window)
        text.pack(expand=True, fill="both")
        text.insert("1.0", history)

    except FileNotFoundError:
        messagebox.showinfo("History", "No history found.")


search_btn = tk.Button(
    root,
    text="🔍 Search Weather",
    font=("Arial", 12),
    width=20,
    command=get_weather
)
search_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="🧹 Clear",
    font=("Arial", 12),
    width=20,
    command=clear_data
)
clear_btn.pack(pady=5)

history_btn = tk.Button(
    root,
    text="📜 View History",
    font=("Arial", 12),
    width=20,
    command=view_history
)
history_btn.pack(pady=5)

exit_btn = tk.Button(
    root,
    text="❌ Exit",
    font=("Arial", 12),
    width=20,
    command=root.destroy
)
exit_btn.pack(pady=5)

root.mainloop()