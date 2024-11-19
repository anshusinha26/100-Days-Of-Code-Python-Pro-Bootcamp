"""imported requests module"""
import requests

"""dictionary to hold the parameters"""
parameters = {
    "amount": 10,
    "type": "boolean"
}

"""variable to store the response"""
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

"""variable to store the data"""
data = response.json()["results"]


question_data = data
