import json

with open('person.json') as file:
    data = json.load(file)

print(data)