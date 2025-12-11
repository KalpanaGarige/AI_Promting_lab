# Prompt:
# write a python function that displays weather details of a city using the OpenWeatherMap
# weather API with error handling. The function must take city name as a parameter.
# Display output in a user-friendly format (not raw JSON).
# Show temperature, humidity, and weather description.
# Handle errors: invalid city, wrong API key, timeout, and network errors.


import requests

def get_weather_details(city):
    API_KEY = "91ed2fa4dbbae86bffc5de4d102bf601"   # ← Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()   # raises error for 401, 404, etc.

        data = response.json()

        # Extract fields
        city_name = data["name"]
        temp_kelvin = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Convert Kelvin → Celsius
        temp_celsius = temp_kelvin - 273.15

        # Display user-friendly output
        print(f"\nCity: {city_name}")
        print(f"Temperature: {temp_celsius:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    # ERROR HANDLING
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city name.")
        elif response.status_code == 401:
            print("Error: Invalid API key. Check your OpenWeatherMap key.")
        else:
            print(f"HTTP Error: {http_err}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Check your internet connection.")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to the API. Please try again later.")

    except KeyError:
        print("Error: Unexpected response format from API.")

    except Exception as e:
        print("Unexpected Error:", e)


# ▶ Example Input
city_name = input("Enter city name: ")
get_weather_details(city_name)
