import mysql.connector
import math
import time

# database connection information
host = "sql7.freesqldatabase.com"
user = "sql7589569"
password = "NTLDAUBVuH"
database = "sql7589569"

# Connect to the database
try:
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    c = conn.cursor()
    # Create a table to store the data
    #c.execute('''CREATE TABLE data
    #            (x real, y real)''')
except mysql.connector.Error as e:
    print(f'Error connecting to the database: {e}')
    conn.close()
    exit()

# Generate and insert sinusoidal data into the table in real-time
x = 0
while True:
    try:
        y1 = 20*math.sin(x)
        y2 = 30*math.sin(x+10)
        c.execute("INSERT INTO molde1 (P1, T1) VALUES (%s, %s)", (y1, y2))
        conn.commit()
        x += 0.1
        time.sleep(1)
    except mysql.connector.Error as e:
        print(f'Error inserting data: {e}')
        conn.close()
        exit()

# Close the connection
conn.close()
