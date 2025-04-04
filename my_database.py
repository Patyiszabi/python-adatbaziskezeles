import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
DATABASE =  "oscar"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

mycursor.execute(f"USE {DATABASE}")


mycursor.execute("SELECT ev, cim FROM film WHERE nyert = 1 ORDER BY ev;")
for x in mycursor:
    print(x)

mycursor.execute("SELECT ev FROM film GROUP BY ev HAVING COUNT(film.id) >= 10;")
for x in mycursor:
    print(x)

mycursor.execute("SELECT cim FROM film WHERE ev BETWEEN 1939 AND 1945;")
for x in mycursor:
    print(x)

mycursor.execute("SELECT cim FROM film WHERE ev BETWEEN 1939 AND 1945;")
for x in mycursor:
    print(x)

mycursor.execute("SELECT cim FROM film WHERE nyert = 1 AND ev + 10 <= bemutato;")
for x in mycursor:
    print(x) 