import MySQLdb
import _mysql_connector
import getopt
try:
    connection = _mysql_connector.connect(
        host='127.0.0.1',
        port = 3306,
        user = 'root',
        password='Giakhang2018@',
        database='flight_game',
    )
except MySQLdb.Error as e:
    print(f"Error connecting to MAriaDB failed: {e}")
    exit(1)
cursor = connection.cursor()
ask = input("Enter the ICAO here: ")

sql = f'select airport.name as "airport name", country.name as "country name" from airport, country where country.iso_country = airport.iso_country and ident = "{ask}"'
cursor.execute(sql)
row = cursor.fetchall()
if len(row) == 0:
    print("There are no results for this ")
else:
    for airport_name, country in row:
        print(f"Airport : {airport_name} \nlocation : {country}")



#2
import _mysql_connector
try:
    connection = _mysql_connector.connect(
        host='127.0.0.1',
        port = 3306,
        user = 'root',
        password='Giakhang2018@',
        database='flight_game',
    )
except MySQLdb.Error  as e:
    print(f"Error connecting to MAriaDB failed: {e}")
    exit(1)
cursor = connection.cursor()
ask = input("Enter the area code: ")

sql = f'select country.name as "country name", type from airport, country where country.iso_country = airport.iso_country and country.iso_country = "{ask}"  ORDER BY airport.type asc';

cursor.execute(sql)
row = cursor.fetchall()
if len(row) == 0:
    print("There are no results for this ")
else:
    for airport_name, country in row:
        print(f"{airport_name}, {country}")

#3
import _mysql_connector
from geopy.distance import geodesic
try:
    connection = _mysql_connector.connect(
        host='127.0.0.1',
        port = 3306,
        user = 'root',
        password='Giakhang2018@',
        database='flight_game',
    )
except MySQLdb.Error as e:
    print(f"Error connecting to MAriaDB failed: {e}")
    exit(1)

cursor = connection.cursor()

ask = input("Enter ICAO of airport 1: ")
sql = f'select latitude_deg, longitude_deg from airport where ident = "{ask}"'
cursor.execute(sql)
row = cursor.fetchall()

ask2 = input("Enter ICAO of airport 2: ")
sql2 = f'select latitude_deg, longitude_deg from airport where ident = "{ask2}"'
cursor.execute(sql2)
row2 = cursor.fetchall()

if len(row) == 0 or len(row2) == 0:
    print("There are no results for this ")
else:
    for la1, lo1 in row:
        location1 = (la1,lo1)
    for la2, lo2 in row2:
        location2 = (la2,lo2)
    distance = geodesic(location1, location2).kilometers
print(f'The distance between 2 airports is {distance}')

kilomet = int(input("Enter kilometers you have traveled: "))
def km_to_lit():
    lit = (kilomet*5)/100
    return lit
a = km_to_lit()
print(f"It costs {a}lit to travel {kilomet}km")
