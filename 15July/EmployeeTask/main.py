import csv
import json
import mysql.connector


try:
    mySQLdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yugam123',
        database='exl'
    )
except mysql.connector.Error as err:
    print(f'====>Error: {err}')
except Exception as err:
    print(f'====>An unexpected error occurred: {err}')



def readCSV(employeeData):
    with open('employees.csv', mode='r', newline='') as csvfile:
        csvReader = csv.reader(csvfile)
        next(csvReader)
        for row in csvReader:
            emp = {
                'emp_id' : int(row[0]),
                'name' : row[1],
                'department' : row[2],
                'salary' : int(int(row[3]) * 1.10),
            }
            employeeData.append(emp)

def modifyEmployeeData(employeeData):
    for emp in employeeData:
        emp['salary'] = emp['salary'] + 10000 if emp['salary'] >= 55000 else emp['salary']
        emp['isEligible'] = True if emp['salary'] >= 55000 else False


def saveToJSON(employeeData):
    with open('employees.json', mode='w') as jsonfile:
        json.dump(employeeData, jsonfile, indent=4)

try:
    cursor = mySQLdb.cursor()

    def insertData(emp_id, name, department, salary):
        sql = 'INSERT INTO employees (`emp_id`, `name`,`department`,`salary`) VALUES (%s, %s, %s, %s)'
        values = (emp_id, name, department, salary)
        cursor.execute(sql, values)
        mySQLdb.commit()

    def storeInDb(employeeData):
        for emp in employeeData:
            insertData(emp['emp_id'], emp['name'], emp['department'], emp['salary'])

    def getAllEmployees():
        sql = 'SELECT * FROM employees'
        cursor.execute(sql)
        employees = cursor.fetchall()
        for emp in employees:
            print(f'Employee ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Salary: {emp[3]}')


except mysql.connector.Error as err:
    print(f'====>Error: {err}')
    mySQLdb.rollback()
except Exception as err:
    print(f'====>An unexpected error occurred: {err}')
    mySQLdb.rollback()


def main():
    employeeData = []
    readCSV(employeeData)
    storeInDb(employeeData)
    getAllEmployees()
    modifyEmployeeData(employeeData)
    saveToJSON(employeeData)

if __name__ == '__main__':
    main()

cursor.close()
mySQLdb.close()
print('MySQL connector is closed')