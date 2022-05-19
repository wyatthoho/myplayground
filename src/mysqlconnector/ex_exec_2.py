import mysql.connector

# Create connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    database='sakila',
    password='password')

# Create cursor
cursor = connection.cursor(dictionary=True)

# Execute
cursor.execute('SELECT * FROM actor;')

# Print
for data in cursor:
    print(data)

# Close
cursor.close()
connection.close()

