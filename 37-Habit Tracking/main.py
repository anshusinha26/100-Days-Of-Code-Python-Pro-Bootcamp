# -------------------- MODULES --------------------
"""imported requests module"""
import requests

"""imported datetime module as dt"""
import datetime as dt

from dotenv import load_dotenv
load_dotenv()
import os


# -------------------- CONSTANTS --------------------
"""contants"""
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_ID = "graph1"


# -------------------- WORKING WITH PIXELA --------------------
"""variable to store endpoint"""
pixelaEndpoint = "https://pixe.la/v1/users"

"""dictionary to hold the parameters"""
pixelaParameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

"""posting the request"""
response = requests.post(url=pixelaEndpoint, json=pixelaParameters)
print(response.text)


# -------------------- WORKING WITH THE GRAPH --------------------
"""variable to store the graph endpoint"""
graphEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs"

"""dictionary to hold the graph parameters"""
graphParameters = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graphEndpoint, json=graphParameters, headers=headers)
# print(response.text)


# -------------------- MAKING A DATA ENTRY --------------------
"""variable to hold dates"""
today = dt.datetime.today().strftime("%Y%m%d")

"""variable to store the data creation endpoint"""
pixelDataCreationEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{GRAPH_ID}"

"""dictionary to hold the data creation parameters"""
pixelDataCreationParameters = {
    "date": today,
    "quantity": "10.5",
}

# response = requests.post(url=pixelDataCreationEndpoint, json=pixelDataCreationParameters, headers=headers)
# print(response.text)


# -------------------- UPDATING A DATA ENTRY --------------------
"""variable to store the update endpoint"""
updateEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

"""dictionary to hold the updated parameters"""
updateParameters = {
    "quantity": "5.2"
}

# response = requests.put(url=updateEndpoint, json=updateParameters, headers=headers)
# print(response.text)


# -------------------- DELETING A DATA ENTRY --------------------
"""variable to store the delete endpoint"""
deleteEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=deleteEndpoint, headers=headers)
# print(response.text)


# -------------------- WORKING WITH DATA ENTRIES--------------------
"""function to work with data entry"""
def workWithData():
    userInput = int(input("""
    Choose from below options:
        1 - Make entry
        2 - Update entry
        3 - Delete entry 
    """))
    if userInput == 1:
        response = requests.post(url=pixelDataCreationEndpoint, json=pixelDataCreationParameters, headers=headers)
        print(response.text)
    elif userInput == 2:
        response = requests.put(url=updateEndpoint, json=updateParameters, headers=headers)
        print(response.text)
    elif userInput == 3:
        response = requests.delete(url=deleteEndpoint, headers=headers)
        print(response.text)
    else:
        print("Invalid input!")

workWithData()



