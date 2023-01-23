import mysql.connector
import math
import time

# database connection information
host = "127.0.0.1"
user = "root"
password = ".,Descobre123"
database = "ddsua2023"

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
    for i in range(10):
        try:
            t1= 20*math.sin(x)
            t2 = 30*math.sin(x+10)
            p1= 20*math.sin(x)
            p2 = 30*math.sin(x+10)
            d1 = 10*math.sin(x)
            d2 = 15*math.sin(x+10)
            d3 = 20*math.sin(x+20)
            accx = 10*math.sin(x)
            accy = 15*math.sin(x+10)
            accz = 20*math.sin(x+20)
            deff = 20*math.sin(x)
            c.execute("INSERT INTO molde1 (T1, T2, P1, P2, D1, D2, D3, ACCX, ACCY, ACCZ, DEF) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (t1, t2, p1, p2, d1, d2, d3, accx, accy, accz, deff))
            
            x += 0.05

            if i == 9:
                c.execute('DELETE FROM molde1;')
                c.execute('ALTER TABLE molde1 AUTO_INCREMENT = 1;')

            conn.commit()
            time.sleep(1)
        except mysql.connector.Error as e:
            print(f'Error inserting data: {e}')
            conn.close()
            exit()

# Close the connection
conn.close()