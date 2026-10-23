import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Added [0] here to grab the first dictionary in the list
        current = data["current_condition"][0]
        temp_c = current["temp_C"]
        condition = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]

        print(f"\n--- Weather Report for {city.title()} ---")
        print(f"Temperature : {temp_c}°C")
        print(f"Condition   : {condition}")
        print(f"Humidity    : {humidity}%")
    else:
        print("Could not find data for that city. Check spelling!")


while True:
    city_input = input("\nEnter a city name (or type 'quit' to exit): ")

    if city_input.lower() == "quit":
        print("Goodbye, Thank you for using weather app pt1")
        break

    get_weather(city_input)
