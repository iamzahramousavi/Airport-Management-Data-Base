import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Airline ("
                                 "ID      INTEGER  NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                                 "carrier VARCHAR(2) NOT NULL,"
                                 "name    VARCHAR(50))"
                                 )
        connect.myDatabase.commit()
        print("TABLE Airline created.")
    except Exception as e:
        print("TABLE Airline ERROR!!!   ", e.args)


def insert(carrier, name):
    try:
        connect.mycursor.execute(f"INSERT INTO Airline (carrier, name) VALUES ('{carrier}', '{name}')")
        connect.myDatabase.commit()
        print("Airline inserted.")
    except:
        print("Airline ERROR!!!")


def update(carrier, name):
    try:
        connect.mycursor.execute(f"UPDATE Airline SET name = '{name}' WHERE carrier = '{carrier}'")
        connect.myDatabase.commit()
        print("Airline updated.")
    except:
        print("Airline ERROR!!!")


def delete(carrier):
    try:
        connect.mycursor.execute(f"DELETE FROM Airline WHERE carrier = '{carrier}'")
        connect.myDatabase.commit()
        print("Airline deleted.")
    except:
        print("Airline ERROR!!!")