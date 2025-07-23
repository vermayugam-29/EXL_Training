import mysql.connector

mySQLdb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'yugam123',
    database = 'exl'
)

cursor = mySQLdb.cursor()
print('Connected to MySQL database')

#Insert data to table
def insertData(name, age):
    sql = 'INSERT INTO person (`name`, `age`) VALUES (%s, %s)'
    values = (name , age)
    cursor.execute(sql, values)
    mySQLdb.commit()
    print('Data inserted')

#Read data
def getAll():
    cursor.execute('SELECT * FROM person')
    result = cursor.fetchall()
    print(result)

#Update Data
def updateData(name, age):
    sql = 'UPDATE person SET age = %s WHERE name = %s'
    values = (age , name)
    cursor.execute(sql, values)
    mySQLdb.commit()
    print('Data updated')

#Delete Data
def deleteUser(name):
    sql = 'DELETE FROM person WHERE name = %s'
    cursor.execute(sql, (name,))
    mySQLdb.commit()
    print('Data deleted')


def main():
    # insertData('Yugam', 22)
    getAll()
    updateData('Yugam', 21)
    # deleteUser('Yugam')
    getAll()


if __name__ == '__main__':
    main()

cursor.close()
mySQLdb.close()
print('MySQL connector is closed')