import psycopg2

# connect to db
connection = psycopg2.connect(database="chinook")

# get cursor from db
cursor = connection.cursor()

# execute select
# cursor.execute('select * from "Artist"')
# cursor.execute('select "Name" from "Artist"')
# cursor.execute('select * from "Artist" where "Name" = %s', ["Queen"])
# cursor.execute('select * from "Album" where "ArtistId" = %s', [51])
cursor.execute('select * from "Track" where "Composer" = %s', ["Queen"])

# fetch multiple results
results = cursor.fetchall()

# fetch single result
# results = cursor.fetchone()

# close connection
connection.close()

for result in results:
    print(result)
