import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Airport ("
                         "Code VARCHAR(3) NOT NULL PRIMARY KEY,"
                         "Name VARCHAR(80) NOT NULL,"
                         "Lat  NUMERIC(15,8) NOT NULL,"
                         "Lon  NUMERIC(15,8) NOT NULL,"
                         "City INTEGER NOT NULL,"
                         "foreign key (City) references City(ID))"
                         )
        connect.myDatabase.commit()
        print("TABLE Airport created.")
    except Exception as e:
        print("TABLE Airport ERROR!!! ", e.args)

# create()

def insert(Code, Name, Lat, Lon):
    try:
        connect.mycursor.execute(f"INSERT INTO Airport (Code, Name, Lat, Lon) VALUES ('{Code}', '{Name}', '{Lat}', '{Lon}')")
        connect.myDatabase.commit()
        print("Airport inserted.")
    except:
        print("Airport ERROR!!!")


def update(Code, Name, Lat, Lon):
    try:
        connect.mycursor.execute(f"UPDATE Airport SET Name = '{Name}', Lat = '{Lat}', Lon = '{Lon}' WHERE Code = '{Code}'")
        connect.myDatabase.commit()
        print("Airport updated.")
    except:
        print("Airport ERROR!!!")


def delete(Code):
    try:
        connect.mycursor.execute(f"DELETE FROM Airport WHERE Code = '{Code}'")
        connect.myDatabase.commit()
        print("Airport deleted.")
    except:
        print("Airport ERROR!!!")
