import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Passenger ("
                         "PassengerID          INTEGER  NOT NULL PRIMARY KEY ,"
                         "FlyerStatus VARCHAR(10),"
                         "foreign key (PassengerID) references Person (ID) on delete cascade )"
                         )
        connect.myDatabase.commit()
        print("TABLE Passenger created.")
    except:
        print("TABLE Passenger ERROR!!! ", e.args)


def insert(PassengerID, FlyerStatus):
    try:
        connect.mycursor.execute(f"INSERT INTO Passenger (PassengerID, FlyerStatus) VALUES ('{PassengerID}', '{FlyerStatus}')")
        connect.myDatabase.commit()
        print("Passenger inserted.")
    except:
        print("Passenger ERROR!!!")


def update(PassengerID, FlyerStatus):
    try:
        connect.mycursor.execute(f"UPDATE Passenger SET FlyerStatus = '{FlyerStatus}' WHERE PassengerID = '{PassengerID}'")
        connect.myDatabase.commit()
        print("Passenger updated.")
    except:
        print("Passenger ERROR!!!")


def delete(PassengerID):
    try:
        connect.mycursor.execute(f"DELETE FROM Passenger WHERE PassengerID = '{PassengerID}'")
        connect.myDatabase.commit()
        print("Passenger deleted.")
    except:
        print("Passenger ERROR!!!")
