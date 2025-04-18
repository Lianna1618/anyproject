import mysql.connector

# Establish a connection
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database",
)

# Create a cursor object
cursor = connection.cursor()

# Example: Execute a query
cursor.execute("SELECT * FROM users")

# Fetch results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
cursor.close()
connection.close()
