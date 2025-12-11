#Prompt: write a python function that displays weather details of a city using weather API with error handling. Display weather details in user-friendly format and also append results into a local file results.json on every run.
import requests
import json
import os

def save_weather(city):
    API_KEY = "91ed2fa4dbbae86bffc5de4d102bf601"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        res = requests.get(url)
        res.raise_for_status()

        data = res.json()

        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        # Display output
        print(f"City: {city_name}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {desc}")

        # Prepare data to append
        new_entry = {
            "city": city_name,
            "temp": temp,
            "humidity": humidity,
            "weather": desc
        }

        # If file exists, load it, else create new list
        if os.path.exists("results.json"):
            with open("results.json", "r") as f:
                content = json.load(f)
        else:
            content = []

        # Append new data
        content.append(new_entry)

        # Save back to file
        with open("results.json", "w") as f:
            json.dump(content, f, indent=4)

        print("\nWeather details saved to results.json")

    except:
        print("Error: Could not fetch weather details.")


city = input("Enter city: ")
save_weather(city)
