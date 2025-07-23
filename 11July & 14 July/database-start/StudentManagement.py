import mysql.connector

try:
    mySQLdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yugam123',
        database='college'
    )
except mysql.connector.Error as err:
    print(f'====>Error: {err}')
except Exception as err:
    print(f'====>An unexpected error occurred: {err}')

cursor = mySQLdb.cursor()
print('Connected to MySQL database')


try:
    def closeDB():
        cursor.close()
        mySQLdb.close()
        print('MySQL connector is closed')

    def addStudent(name ,age, department, percentage):
        sql = 'INSERT INTO students (`name`, `age`, `department`, `percentage`) VALUES (%s, %s, %s, %s)'
        values = (name , age , department , percentage)
        cursor.execute(sql, values)
        mySQLdb.commit()
        print(f"{name}'s data inserted")

    def getAllStudents():
        sql = 'SELECT * FROM students'
        cursor.execute(sql)
        students = cursor.fetchall()
        for student in students:
            print(student)

    def updateStudentAge(name, age):
        sql = 'UPDATE students SET age = %s WHERE name = %s'
        values = (age, name)
        cursor.execute(sql, values)
        mySQLdb.commit()
        print(f"{name}'s age updated")

    def updateStudentDepartment(name, department):
        sql = 'UPDATE students SET department = %s WHERE name = %s'
        values = (department, name)
        cursor.execute(sql, values)
        mySQLdb.commit()
        print(f"{name}'s department updated")

    def updateStudentPercentage(name, percentage):
        sql = 'UPDATE students SET percentage = %s WHERE name = %s'
        values = (percentage, name)
        cursor.execute(sql, values)
        mySQLdb.commit()
        print(f"{name}'s percentage updated")

    def updateStudentName(name, newName):
        sql = 'UPDATE students SET name = %s WHERE name = %s'
        values = (newName, name)
        cursor.execute(sql, values)
        mySQLdb.commit()

        if cursor.rowcount == 0:
            print(f"No such name is present in the entries")
        else:
            print(f"{name}'s name updated to {newName}")

    def deleteStudent(name):
        sql = 'DELETE FROM students WHERE `name` = %s'
        cursor.execute(sql, (name,))
        mySQLdb.commit()
        print(f"{name}'s record deleted")

    def getByName(name):
        sql = 'SELECT * FROM students WHERE `name` = %s'
        cursor.execute(sql, (name,))
        students = cursor.fetchall()
        for student in students:
            print(student)
except mysql.connector.Error as err:
    print(f'====>Error: {err}')
except Exception as err:
    print(f'====>An unexpected error occurred: {err}')



def main():
    while True:
        print('\n===== Student Management Menu =====')
        print('1. Add Student')
        print('2. View All Students')
        print('3. Update Student Name')
        print('4. Update Student Age')
        print('5. Update Student Department')
        print('6. Update Student Percentage')
        print('7. Delete Student')
        print('8. Search Student by Name')
        print('9. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter Name: ')
            age = int(input('Enter Age: '))
            department = input('Enter Department: ')
            percentage = float(input('Enter Percentage: '))
            addStudent(name, age, department, percentage)

        elif choice == '2':
            getAllStudents()

        elif choice == '3':
            name = input('Enter Current Name: ')
            newName = input('Enter New Name: ')
            updateStudentName(name, newName)

        elif choice == '4':
            name = input('Enter Name: ')
            age = int(input('Enter New Age: '))
            updateStudentAge(name, age)

        elif choice == '5':
            name = input('Enter Name: ')
            department = input('Enter New Department: ')
            updateStudentDepartment(name, department)

        elif choice == '6':
            name = input('Enter Name: ')
            percentage = float(input('Enter New Percentage: '))
            updateStudentPercentage(name, percentage)

        elif choice == '7':
            name = input('Enter Name to Delete: ')
            deleteStudent(name)

        elif choice == '8':
            name = input('Enter Student Name to Search: ')
            getByName(name)

        elif choice == '9':
            print('Exiting...')
            break

        else:
            print('Invalid choice! Please select a valid option.')



if __name__ == '__main__':
    main()

closeDB()