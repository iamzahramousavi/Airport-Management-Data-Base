import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE RouteServe ("
                         "ID           INTEGER  NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                         "Flight       INTEGER  NOT NULL,"
                         "Origin       VARCHAR(3)  NOT NULL,"
                         "Dest         VARCHAR(3)  NOT NULL,"
                         "foreign key (Flight) references Flight (ID) on delete cascade,"
                         "foreign key (Origin, Dest) references Route (Origin, Dest) on delete cascade)"
                         )

        connect.myDatabase.commit()
        print("TABLE RouteServe created.")
    except Exception as e:
        print("TABLE RouteServe ERROR!!! ", e.args)

# create()

def insert(Date, FlightNumber, SchedArrTime, SchedDepTime, Origin, Dest):
    try:
        connect.mycursor.execute(f"INSERT INTO RouteServe (Date, FlightNumber, SchedArrTime, SchedDepTime, Origin, Dest) VALUES ('{Date}', '{FlightNumber}', '{SchedArrTime}', '{SchedDepTime}', '{Origin}', '{Dest}')")
        connect.myDatabase.commit()
        print("RouteServe inserted.")
    except:
        print("RouteServe ERROR!!!")


def update(Date, FlightNumber, SchedArrTime, SchedDepTime, Origin, Dest):
    try:
        connect.mycursor.execute(f"UPDATE RouteServe SET Origin = '{Origin}', Dest = '{Dest}' WHERE Date = '{Date}' AND FlightNumber = '{FlightNumber}' AND SchedArrTime = '{SchedArrTime}' AND SchedDepTime = '{SchedDepTime}' AND Origin = '{Origin}' AND Dest = '{Dest}'")
        connect.myDatabase.commit()
        print("RouteServe updated.")
    except:
        print("RouteServe ERROR!!!")


def delete(Date, FlightNumber, SchedArrTime, SchedDepTime, Origin, Dest):
    try:
        connect.mycursor.execute(f"DELETE FROM RouteServe WHERE Date = '{Date}' AND FlightNumber = '{FlightNumber}' AND SchedArrTime = '{SchedArrTime}' AND SchedDepTime = '{SchedDepTime}' AND Origin = '{Origin}' AND Dest = '{Dest}'")
        connect.myDatabase.commit()
        print("RouteServe deleted.")
    except:
        print("RouteServe ERROR!!!")
