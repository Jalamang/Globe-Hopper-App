import dbconn

myCursor = dbconn.con.cursor()

myCursor.execute("USE globehopperapp")

sql = "INSERT INTO Country(CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
val = ('1', 'Canada', '30000000', 'North America');

myCursor.execute(sql,val)


myCursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (2, 'USA', 330000000, 'North America')");
myCursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (3, 'France', 3000000, 'Europe')");
myCursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (4, 'India', 300000000, 'Asia')");

myCursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (1, 'Ottawa', 1, 1, 'Parliament House', 'Museum', 'Rideau Canal')");
myCursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (2, 'Toronto', 1, 0, 'CN Tower', 'Niagara Falls', 'AGO')");
myCursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (3, 'Washington', 2, 1, 'White House', 'Lincoln Memorial', 'National Air and Space Museum')");

dbconn.con.commit()
print(myCursor.rowcount, "record inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)