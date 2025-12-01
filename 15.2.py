#Prompt: write a python function that displays weather details of a city using the OpenWeatherMap weather API with proper error handling. Display output as formatted JSON. Use try/except to handle invalid URL, network timeout, wrong API key, or invalid responses.
import requests
import json

def get_weather_with_error_handling(city):
    API_KEY ="91ed2fa4dbbae86bffc5de4d102bf60"    # Replace with your actual key
      # 🔴 Replace this with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url, timeout=5)   # timeout handling
        response.raise_for_status()               # handles HTTP errors (401, 404 etc.)

        data = response.json()
        print("Weather Data (JSON):")
        print(json.dumps(data, indent=4))         # pretty JSON output

    except requests.exceptions.Timeout:
        print("Error: API request timed out. Please check your network connection.")

    except requests.exceptions.HTTPError as http_err:
        print(f"Error: HTTP error occurred → {http_err}")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

    except Exception as e:
        print("Unexpected Error:", e)


# ▶ Example Run
city_name = input("Enter a city name: ")
get_weather_with_error_handling(city_name)
