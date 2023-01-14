import connect
from tables import tables


def create_tables():
    try:
        # *****************************************
        # **************  creat  ******************
        # *****************************************
        tables.Person.create()
        tables.Phone.create()
        tables.Passenger.create()
        tables.Airline.create()
        tables.Pilot.create()
        tables.FlightAttendant.create()
        tables.Airplane.create()
        tables.City.create()
        tables.Airport.create()
        tables.Flight.create()
        tables.Route.create()
        tables.Take.create()
        tables.RouteServe.create()

        connect.myDatabase.commit()
        print("Database full Created.")
        print("######################")
    except:
        print("Database creation ERROR!!!")
        print("##########################")
        connect.myDatabase.rollback()
    # finally:
    #     if connect.myDatabase:
    #         connect.myDatabase.close()




def drop_database():
    try:
        connect.mycursor.execute(
            "DROP DATABASE airport_database"
        )
        connect.myDatabase.commit()
        print("DATABASE DROPED.")
    except:
        print("DATABASE DROP ERROR!!!")
        connect.myDatabase.rollback()
    finally:
        if connect.myDatabase:
            connect.myDatabase.close()
