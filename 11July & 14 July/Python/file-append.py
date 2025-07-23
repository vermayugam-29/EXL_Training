import csv

def append_csv():
    persons = [
        ['Yugam', 21, 'Male'],
        ['Raghav', 22, 'Female']
    ]

    with open('data.csv', 'a', newline='') as file:
        prevData = csv.writer(file)
        prevData.writerows(persons)

    print('Data appended')

append_csv()