import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Person ("
                         "ID          INTEGER  NOT NULL PRIMARY KEY AUTO_INCREMENT AUTO_INCREMENT,"
                         "FirstName   VARCHAR(20),"
                         "LastName    VARCHAR(20),"
                         "Sex         VARCHAR(10),"
                         "Address     VARCHAR(50),"
                         "DateOfBirth DATE,"
                         "Occupation  VARCHAR(50),"
                         "City        VARCHAR(50) )"
                         )
        connect.myDatabase.commit()
        print("TABLE Person created.")
    except:
        print("TABLE Person ERROR!!! ", e.args)


def insert(id, firstName, lastName, sex, address, dateOfBirth, occupation, city):
    try:
        connect.mycursor.execute(f"INSERT INTO Person (ID, FirstName, LastName, Sex, Address, DateOfBirth, Occupation, City) VALUES ('{id}','{firstName}','{lastName}','{sex}', '{address}','{dateOfBirth}','{occupation}','{city}')")
        connect.myDatabase.commit()
        print("Person inserted.")
    except:
        print("Person ERROR!!!")


def update(id, firstName, lastName, sex, address, dateOfBirth, occupation, city):
    try:
        connect.mycursor.execute(f"UPDATE Person SET ID = '{id} WHERE FirstName = '{firstName}' AND LastName = '{lastName}' AND Sex = '{sex}' AND Address = '{address}' AND DateOfBirth = '{dateOfBirth}' AND Occupation = '{occupation}' AND City = '{city}'")
        connect.myDatabase.commit()
        print("Person updated.")
    except:
        print("Person ERROR!!!")


def delete(id, firstName, lastName, sex, address, dateOfBirth, occupation, city):
    try:
        connect.mycursor.execute(f"DELETE FROM Person WHERE ID = '{id} AND FirstName = '{firstName}' AND LastName = '{lastName}' AND Sex = '{sex}' AND Address = '{address}' AND DateOfBirth = '{dateOfBirth}' AND Occupation = '{occupation}' AND City = '{city}'")
        connect.myDatabase.commit()
        print("Person deleted.")
    except:
        print("Person ERROR!!!")
