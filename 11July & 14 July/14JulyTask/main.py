import csv
import json
import xml.etree.ElementTree as ET

data = []

def readCSV():
    with open('student.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

def updateData():
    for row in data[1:]:
        row[2] = str(int(row[2]) + 5)
        row[3] = str(int(row[3]) + 5)
        row[4] = str(int(row[4]) + 5)
        row[0] = 'Mr. ' + row[0] if row[5] == 'Male' else 'Ms. ' + row[0]

def storeInXML():
    root = ET.Element('Students')

    for s in data[1:]:
        student = ET.SubElement(root, 'Student')
        ET.SubElement(student, 'Name').text = s[0]
        ET.SubElement(student, 'Age').text = s[1]
        marks = ET.SubElement(student, 'Marks')
        ET.SubElement(marks, 'Math').text = s[2]
        ET.SubElement(marks, 'Science').text = s[3]
        ET.SubElement(marks, 'English').text = s[4]
        ET.SubElement(student, 'Gender').text = s[5]

    tree = ET.ElementTree(root)
    tree.write('students.xml')
    print('Successfully stored in XML file.')

def storeInJSON():
    rows = data[1:]

    newData = []

    for row in rows:
        student = {}

        student['Name'] = row[0]
        student['Age'] = row[1]

        marks = {}
        marks['Math'] = row[2]
        marks['Science'] = row[3]
        marks['English'] = row[4]
        student['Marks'] = marks

        student['Gender'] = row[5]

        newData.append(student)

    with open('students.json', 'w') as file:
        json.dump(newData, file, indent=4)
        print("Successfully stored in JSON file.")



readCSV()
updateData()
storeInXML()
storeInJSON()