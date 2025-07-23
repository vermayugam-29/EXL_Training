import csv

def create_csv():
    persons = [
        ['Name', 'Age', 'Gender'],
        ['Tanmay', 21, 'Male'],
        ['Askhit', 22, 'Female']
    ]
    with open('data2.csv', 'x', newline='') as file:
        createFile = csv.writer(file)
        createFile.writerows(persons)

    print('Created data2.csv')

create_csv()