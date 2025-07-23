import mysql.connector

try:
    mySQLdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yugam123',
        database='exl'
    )
    cursor = mySQLdb.cursor()


    sql = 'UPDATE person SET age = %s WHERE id = %s'
    cursor.execute(sql, (22, 9))
    mySQLdb.commit()

    sqlInsert = 'INSERT INTO person (name, age) VALUES (%s, %s)'
    cursor.execute(sqlInsert, ("Modi Bhaji", 16))

    # sqlSelect = "SELECT * FROM person WHERE id = %s"
    # cursor.execute(sqlSelect, (1,))
    # result = cursor.fetchall()
    # for row in result:
    #     print("ID:", row[0], "Name:", row[1], "Age:", row[2])

    mySQLdb.commit()
    print('Data inserted and updated')
except mysql.connector.Error as err:
    print(err)
    mySQLdb.rollback()
except Exception as err:
    print(err)
    mySQLdb.rollback()
finally:
    print('Attempting to close connection')
    if mySQLdb.is_connected():
        cursor.close()
        mySQLdb.close()
        print('Database connection closed')

print('Ending the program')

