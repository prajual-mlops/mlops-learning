import requests
import json

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

user = response.json()

with open("user_data.json","w") as file:
    json.dump(user, file, indent=4)

print("User data saved successfully")
