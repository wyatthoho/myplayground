import pymysql.cursors
from pymysql import Error


try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        database='sakila',
        password='password')

    if connection.open:
        db_Info = connection.get_server_info()
        print('DB version: ', db_Info)

        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print('Current DB: ', record)

except Error as e:
    print('DB connection failed: ', e)

finally:
    if connection.open:
        cursor.close()
        connection.close()
        print('DB connection closed.')