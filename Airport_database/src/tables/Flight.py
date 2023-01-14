import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Flight ("
                         "ID           INTEGER  NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                         "Date         DATE     NOT NULL,"
                         "FlightNumber INTEGER  NOT NULL,"
                         "SchedArrTime INTEGER  NOT NULL,"
                         "SchedDepTime INTEGER  NOT NULL,"
                         "DepTime      INTEGER  NOT NULL,"
                         "ArrTime      INTEGER  NOT NULL,"
                         "Distance     INTEGER  NOT NULL,"
                         "Airline      INTEGER NOT NULL,"
                         "Airplane     VARCHAR(6) NOT NULL,"
                         "foreign key (Airline) references Airline (ID) on delete cascade,"
                         "foreign key (Airplane) references Airplane (tailnum) on delete cascade)"
                         )
        connect.myDatabase.commit()
        print("TABLE Flight created.")
    except Exception as e:
        print("TABLE Flight ERROR!!! ", e.args)


def insert(Date, FlightNumber, SchedArrTime, SchedDepTime, DepTime, ArrTime, Distance):
    try:
        connect.mycursor.execute(f"INSERT INTO Flight (Date, FlightNumber, SchedArrTime, SchedDepTime, DepTime, ArrTime, Distance) VALUES ('{Date}', '{FlightNumber}', '{SchedArrTime}', '{SchedDepTime}', '{DepTime}', '{ArrTime}', '{Distance}')")
        connect.myDatabase.commit()
        print("Flight inserted.")
    except:
        print("Flight ERROR!!!")


def update(Date, FlightNumber, SchedArrTime, SchedDepTime, DepTime, ArrTime, Distance):
    try:
        connect.mycursor.execute(f"UPDATE Flight SET DepTime = '{DepTime}', ArrTime = '{ArrTime}', Distance = '{Distance}' WHERE Date = '{Date}' AND FlightNumber = '{FlightNumber}' AND SchedArrTime = '{SchedArrTime}' AND SchedDepTime = '{SchedDepTime}'")
        connect.myDatabase.commit()
        print("Flight updated.")
    except:
        print("Flight ERROR!!!")


def delete(Date, FlightNumber, SchedArrTime, SchedDepTime, DepTime, ArrTime, Distance):
    try:
        connect.mycursor.execute(f"DELETE FROM Flight WHERE Date = '{Date}' AND FlightNumber = '{FlightNumber}' AND SchedArrTime = '{SchedArrTime}' AND SchedDepTime = '{SchedDepTime}' AND DepTime = '{DepTime}' AND ArrTime = '{ArrTime}' AND Distance = '{Distance}'")
        connect.myDatabase.commit()
        print("Flight deleted.")
    except:
        print("Flight ERROR!!!")
