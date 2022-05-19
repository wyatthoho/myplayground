import mysql.connector

# Create connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    database='sakila',
    password='password')

# Create cursor
cursor = connection.cursor()

# fetchall
cursor.execute('SELECT * FROM actor;')
record = cursor.fetchall()
print(record)

# fetchone
cursor.execute('SELECT * FROM actor;')
record = cursor.fetchone()
print(record)
record = cursor.fetchone()
print(record)

# fetchmany
cursor.execute('SELECT * FROM actor;')
record = cursor.fetchmany(3)
print(record)

# Close
cursor.close()
connection.close()

