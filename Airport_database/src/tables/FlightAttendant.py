import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE FlightAttendant ("
                         "FAID           INTEGER  NOT NULL PRIMARY KEY,"
                         "YearsOfService INTEGER,"
                         "Salary         INTEGER,"
                         "Rank           VARCHAR(10),"
                         "foreign key (FAID) references Person (ID) on delete cascade )"
                         )
        connect.myDatabase.commit()
        print("TABLE FlightAttendant created.")
    except Exception as e:
        print("TABLE FlightAttendant ERROR!!! ", e.args)


def insert(FAID, YearsOfService, Salary, Rank):
    try:
        connect.mycursor.execute(f"INSERT INTO FlightAttendant (FAID, YearsOfService, Salary, Rank) VALUES ('{FAID}', '{YearsOfService}', '{Salary}', '{Rank}')")
        connect.myDatabase.commit()
        print("FlightAttendant inserted.")
    except:
        print("FlightAttendant ERROR!!!")


def update(FAID, YearsOfService, Salary, Rank):
    try:
        connect.mycursor.execute(f"UPDATE FlightAttendant SET YearsOfService = '{YearsOfService}', Salary = '{Salary}', Rank = '{Rank}' WHERE FAID = '{FAID}'")
        connect.myDatabase.commit()
        print("FlightAttendant updated.")
    except:
        print("FlightAttendant ERROR!!!")


def delete(FAID):
    try:
        connect.mycursor.execute(f"DELETE FROM FlightAttendant WHERE FAID = '{FAID}'")
        connect.myDatabase.commit()
        print("FlightAttendant deleted.")
    except:
        print("FlightAttendant ERROR!!!")
