import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
DATABASE =  "mydatabase"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

mycursor.execute(f"USE {DATABASE}")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")



query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(query, val)
mydb.commit()

mycursor.execute("SELECT * FROM customers WHERE name='Amy'")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM customers WHERE address= 'One way 98'")
for x in mycursor:
    print(x)
