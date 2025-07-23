import xml.etree.ElementTree as ET

tree = ET.parse('persons.xml')
root = tree.getroot()

for person in root.findall('Person'):
    name = person.find('Name').text
    age = person.find('Age').text
    gender = person.find('Gender').text
    print(f'Name: {name}, Age: {age}, Gender: {gender}')
