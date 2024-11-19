# Day1 Project: Band name generator

"""this print statement prints the initial game text"""
print("Welcome to the Band Name Generator!")
"""this variable stores the name of the city given by the user"""
city = input("Enter the name of the city: ")
"""this print statement prints the city name"""
print(city)
"""this variable stores the name of the pet given by the user"""
petName = input("Enter the name of the pet: ")
"""this print statement prints the name of the pet"""
print(petName)
"""this print statement prints the final band name by concatenating both city as well as petname"""
print(f"Your band name could be {city} {petName}")