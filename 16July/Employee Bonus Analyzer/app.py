import csv
import json

def readCSV(data):
    with open('employee_data.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append({
                'id': row[0],
                'name': row[1],
                'experience': row[2],
                'salary': row[3],
                'department': row[4],
                'bonus' : int(int(row[3]) * 0.1) if int(row[2]) > 5 and row[4] == 'Finance' else 0,
            })

def writeInJSON(data):
    with open('employee_data_with_bonus.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def main():
    data = []
    readCSV(data)
    writeInJSON(data)

if __name__ == '__main__':
    main()