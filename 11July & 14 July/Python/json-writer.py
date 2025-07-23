import json

person = {'name' : 'tanmay', 'age' : 22, 'gender' :'male'}

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

print('JSON data written successfully')