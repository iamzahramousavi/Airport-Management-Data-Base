import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Airplane ("
                         "tailnum      VARCHAR(6) NOT NULL PRIMARY KEY,"
                         "year         INTEGER,"
                         "manufacturer VARCHAR(50),"
                         "Model        VARCHAR(50),"
                         "seats        INTEGER ,"
                         "Airline      INTEGER,"
                         "FOREIGN KEY (Airline) REFERENCES Airline (ID) ON DELETE CASCADE )"
                         )
                         
        connect.myDatabase.commit()
        print("TABLE Airplane created.")
    except Exception as e:
        print("TABLE Airplane ERROR!!! ", e.args)


def insert(tailnum, year, manufacturer, Model, seats):
    try:
        connect.mycursor.execute(f"INSERT INTO Airplane (tailnum, year, manufacturer, Model, seats) VALUES ('{tailnum}', '{year}', '{manufacturer}', '{Model}', '{seats}')")
        connect.myDatabase.commit()
        print("Airplane inserted.")
    except:
        print("Airplane ERROR!!!")


def update(tailnum, year, manufacturer, Model, seats):
    try:
        connect.mycursor.execute(f"UPDATE Airplane SET year = '{year}', manufacturer = '{manufacturer}', Model = '{Model}', seats = '{seats}' WHERE tailnum = '{tailnum}'")
        connect.myDatabase.commit()
        print("Airplane updated.")
    except:
        print("Airplane ERROR!!!")


def delete(tailnum):
    try:
        connect.mycursor.execute(f"DELETE FROM Airplane WHERE tailnum = '{tailnum}'")
        connect.myDatabase.commit()
        print("Airplane deleted.")
    except:
        print("Airplane ERROR!!!")
