import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Take ("
                         "ID           INTEGER  NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                         "Type         VARCHAR(20) NOT NULL,"
                         "Class        VARCHAR(50) NOT NULL,"
                         "PassengerID  INTEGER NOT NULL,"
                         "Flight     INTEGER NOT NULL,"
                         "foreign key (Flight) references Flight (ID) on delete cascade,"
                         "foreign key (PassengerID) references Passenger (PassengerID) on delete cascade)"
                         )
        connect.myDatabase.commit()
        print("TABLE Take created.")
    except Exception as e:
        print("TABLE Take ERROR!!! ", e.args)

def insert(Date, FlightNumber, SchedArrTime, SchedDepTime, PassengerID, Type, Class):
    try:
        connect.mycursor.execute(f"INSERT INTO Take (Date, FlightNumber, SchedArrTime, SchedDepTime, PassengerID, Type, Class) VALUES ('{Date}', '{FlightNumber}', '{SchedArrTime}', '{SchedDepTime}', '{PassengerID}', '{Type}', '{Class}')")
        connect.myDatabase.commit()
        print("Take inserted.")
    except:
        print("Take ERROR!!!")


def update(Date, FlightNumber, SchedArrTime, SchedDepTime, PassengerID, Type, Class):
    try:
        connect.mycursor.execute(f"UPDATE Take SET Type = '{Type}', Class = '{Class}' WHERE Date = '{Date}' AND FlightNumber = '{FlightNumber}' AND SchedArrTime = '{SchedArrTime}' AND SchedDepTime = '{SchedDepTime}' AND PassengerID = '{PassengerID}'")
        connect.myDatabase.commit()
        print("Take updated.")
    except:
        print("Take ERROR!!!")


def delete(Date, FlightNumber, SchedArrTime, SchedDepTime, PassengerID, Type, Class):
    try:
        connect.mycursor.execute(f"DELETE FROM Take WHERE Date = '{Date}' AND FlightNumber = '{FlightNumber}' AND SchedArrTime = '{SchedArrTime}' AND SchedDepTime = '{SchedDepTime}' AND PassengerID = '{PassengerID}'")
        connect.myDatabase.commit()
        print("Take deleted.")
    except:
        print("Take ERROR!!!")
