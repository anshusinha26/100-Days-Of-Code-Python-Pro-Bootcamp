# -------------------- MODULES --------------------
"""imported requests module"""
import requests

"""imported datetime module as dt"""
import datetime as dt

from dotenv import load_dotenv
load_dotenv()
import os

# -------------------- WORKING WITH NUTRTIONIX --------------------
"""variables to store the id and api key"""
import requests

nuApiId = os.getenv("NUTRITIONIX_API_ID")
nuApiKey = os.getenv("NUTRITIONIX_API_KEY")

"""variable to store the endpoint"""
nuEndpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

"""dictionary to hold the headers"""
headers = {
    "x-app-id": nuApiId,
    "x-app-key": nuApiKey
}

"""dictionary to hold the parameters"""
nuParameters = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 55,
    "height_cm": 170,
    "age": 19
}

"""variable to hold the response"""
nuResponse = requests.post(url=nuEndpoint, json=nuParameters, headers=headers)
nuData = nuResponse.json()


# -------------------- WORKING WITH SHEETY --------------------
"""getting time"""
time = dt.datetime.now().strftime("%X")

"""getting date"""
date = dt.datetime.now().strftime("%d/%m/%Y")

"""variable to store the endpoint"""
shEndpoint = "https://api.sheety.co/ca1f37009612162d30a52c2a7eb8a469/myWorkouts/workouts"
sheety_api = os.getenv("SHEETY_API_KEY")

bearerHeaders = {
    "Authorization": f"Bearer {sheety_api}"
}

for exercise in nuData["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=shEndpoint, json=sheet_inputs, headers=bearerHeaders)

    print(sheet_response.text)


