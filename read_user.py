import json

with open("user_data.json","r") as file:
    user = json.load(file)

print("Name:", user["name"])
print("Email:", user["email"] )
