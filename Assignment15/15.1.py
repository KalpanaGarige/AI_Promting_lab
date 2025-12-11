
# write a python function that display weather details of a city using weather api without error handling.
# Display weather details as JSON output.

import requests
import json

def get_weather(city):
    """
    Task 1:
    Connects to OpenWeatherMap API and retrieves weather details
    with NO error handling (as required).
    Displays the output in pretty JSON format.
    """

    api_key = "91ed2fa4dbbae86bffc5de4d102bf601"    # Replace with your actual key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)          # No try-except here
    data = response.json()                # Parse JSON

    # Pretty display JSON output
    print(json.dumps(data, indent=4))


# Example run
get_weather("London")
