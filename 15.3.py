# Prompt: write a python function that uses the OpenWeatherMap API and extracts
# specific weather details (temperature, humidity, description) from the API response.
# Display the output in a clean user-friendly format. Include error handling for invalid
# city names, wrong API key, timeouts, and network errors.
import requests

def get_weather_details(city):
    API_KEY = "91ed2fa4dbbae86bffc5de4d102bf601"   # ← Use your valid key here
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # triggers error for 401, 404 etc.

        data = response.json()

        # Extract required fields
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()
        city_name = data["name"]

        # User-friendly output
        print("\nWeather Report")
        print("---------------------------")
        print(f"City: {city_name}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

    except requests.exceptions.HTTPError as err:
        print("Error: Invalid city name or wrong API key!")
        print("Details:", err)

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to the API. Check your internet or API key.")

    except KeyError:
        print("Error: Unable to extract weather details. API returned unexpected data.")


# ▶ Example Run
city = input("Enter city name: ")
get_weather_details(city)
