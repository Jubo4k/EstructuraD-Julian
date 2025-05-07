import json


with open(r'C:\Users\306\Desktop\EST\clas\JSON', 'r') as file:
    data = json.load(file)  # Cargar los datos desde el archivo



# 1. Extract the name of the first motorcycle model
first_model_name = data['models'][0]['name']
print(f"First Motorcycle Model: {first_model_name}")

# 2. Extract the horsepower of the second motorcycle model (MT-07)
second_model_horsepower = data['models'][1]['engine']['horsepower']
print(f"Second Motorcycle Model (MT-07) Horsepower: {second_model_horsepower} HP")

# 3. Extract the contact email for the dealer in Los Angeles
dealer_email = data['dealerLocations'][0]['contact']['email']
print(f"Dealer Email in Los Angeles: {dealer_email}")
