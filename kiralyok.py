from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='kiralyok')

cursor = cnx.cursor()


cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
print()


cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)
print()

cursor.execute('''SELECT uralkodo.nev, uralkodo.ragnev, uralkodo.szul FROM uralkodo
WHERE uralkodo.ragnev IS NOT NULL
ORDER BY uralkodo.szul ASC''')
for uralkodo in cursor:
    print(uralkodo)
print()

cursor.execute('''SELECT uralkodo.nev, hivatal.mettol, hivatal.meddig
FROM uralkodo
JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az
JOIN uralkodohaz ON uralkodo.uhaz_az = uralkodohaz.azon
WHERE uralkodohaz.nev = 'Árpád-ház'
ORDER BY hivatal.mettol ASC''')
for uralkodo in cursor:
    print(uralkodo)
print()

cursor.execute('''SELECT uralkodo.nev FROM uralkodo
JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az
WHERE hivatal.koronazas > hivatal.mettol
AND hivatal.koronazas IS NOT NULL''')
for uralkodo in cursor:
    print(uralkodo)
print()

cursor.execute('''SELECT COUNT(DISTINCT hivatal.uralkodo_az) FROM hivatal
WHERE (hivatal.mettol BETWEEN 1601 AND 1700)
OR (hivatal.meddig BETWEEN 1601 AND 1700)''')
for uralkodo in cursor:
    print(uralkodo)

cursor.execute('''SELECT uralkodo.nev, MAX(hivatal.meddig - hivatal.mettol) AS uralkodasi_ido
FROM uralkodo
JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az
GROUP BY uralkodo.nev
ORDER BY uralkodasi_ido DESC
LIMIT 1''')
for uralkodo in cursor:
    print(uralkodo)
print()

cursor.execute('''SELECT uralkodo.nev, (hivatal.mettol - uralkodo.szul) AS eletkor
FROM uralkodo
JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az
WHERE (hivatal.mettol - uralkodo.szul) < 15
ORDER BY eletkor ASC''')
for uralkodo in cursor:
    print(uralkodo)
print()

cursor.execute('''SELECT uralkodo.nev, SUM(hivatal.meddig - hivatal.mettol) AS uralkodasi_ido
FROM uralkodo
JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az
GROUP BY uralkodo.nev
HAVING COUNT(hivatal.azon) > 1''')
for uralkodo in cursor:
    print(uralkodo)
print()

cursor.execute('''SELECT uralkodohaz.nev, COUNT(DISTINCT uralkodo.azon) AS uralkodok_szama
FROM uralkodo
JOIN uralkodohaz ON uralkodo.uhaz_az = uralkodohaz.azon
GROUP BY uralkodohaz.nev
ORDER BY uralkodok_szama DESC''')
for uralkodo in cursor:
    print(uralkodo)



cursor.close()
cnx.close()