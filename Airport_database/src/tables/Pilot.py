import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Pilot ("
                         "PilotID        INTEGER  NOT NULL PRIMARY KEY,"
                         "YearsOfService INTEGER,"
                         "Salary         INTEGER,"
                         "Airline        INTEGER NOT NULL,"
                         "foreign key (Airline) references Airline (ID) on delete cascade,"
                         "foreign key (PilotID) references Person (ID) on delete cascade )"
                         )
        connect.myDatabase.commit()
        print("TABLE Pilot created.")
    except Exception as e:
        print("TABLE Pilot ERROR!!! ", e.args)

# create()

def insert(PilotID, YearsOfService, Salary):
    try:
        connect.mycursor.execute(f"INSERT INTO Pilot (PilotID, YearsOfService, Salary) VALUES ('{PilotID}', '{YearsOfService}', '{Salary}')")
        connect.myDatabase.commit()
        print("Pilot inserted.")
    except:
        print("Pilot ERROR!!!")


def update(PilotID, YearsOfService, Salary):
    try:
        connect.mycursor.execute(f"UPDATE Pilot SET YearsOfService = '{YearsOfService}', Salary = '{Salary}' WHERE PilotID = '{PilotID}'")
        connect.myDatabase.commit()
        print("Pilot updated.")
    except:
        print("Pilot ERROR!!!")


def delete(PilotID):
    try:
        connect.mycursor.execute(f"DELETE FROM Pilot WHERE PilotID = '{PilotID}'")
        connect.myDatabase.commit()
        print("Pilot deleted.")
    except:
        print("Pilot ERROR!!!")
