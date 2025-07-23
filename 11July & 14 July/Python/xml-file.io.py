import xml.etree.ElementTree as ET

def xmlTree():
    persons = [
        {'Name': 'Yugam', 'Age' : 21, 'Gender' : 'Male'},
        {'Name': 'Raghav', 'Age' : 22, 'Gender' : 'Female'},
        {'Name': 'Akshit', 'Age' : 22, 'Gender' : 'Others'},
    ]

    root = ET.Element('Persons')

    for p in  persons:
        person = ET.SubElement(root, 'Person')
        ET.SubElement(person, 'Name').text = p['Name']
        ET.SubElement(person, 'Age').text = str(p['Age'])
        ET.SubElement(person, 'Gender').text = p['Gender']

    tree = ET.ElementTree(root)

    tree.write('persons.xml')

    print("Data written successfully")

xmlTree()