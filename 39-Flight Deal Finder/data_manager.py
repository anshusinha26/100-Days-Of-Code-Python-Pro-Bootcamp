import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ca1f37009612162d30a52c2a7eb8a469/flightDeals/prices"
headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        if response.status_code == 200:
            data = response.json()
            pprint(data)
            if "prices" in data:
                self.destination_data = data["prices"]
            else:
                print("Error: 'prices' key not found in API response.")
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers  # Use headers instead of auth
            )
            print(response.text)
