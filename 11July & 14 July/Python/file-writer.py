import csv

def write_csv():
    persons = [
        ['Name', 'Age', 'Gender'],
        ['Tanmay', 21, 'Male'],
        ['Askhit', 22, 'Female']
    ]

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(persons)

    print('Data written Successful')

write_csv()
