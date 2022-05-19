import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        database='sakila',
        password='password')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print('DB version: ', db_Info)

        cursor = connection.cursor()
        cursor.execute('SELECT DATABASE();')
        record = cursor.fetchone()
        print('Current DB: ', record)

except Error as e:
    print('DB connection failed: ', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('DB connection closed.')