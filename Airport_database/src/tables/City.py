import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE City ("
                         "ID         INTEGER  NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                         "Name       VARCHAR(50) NOT NULL,"
                         "Country    VARCHAR(20) NOT NULL,"
                         "Population INTEGER  NOT NULL,"
                         "Area       NUMERIC(20,2) NOT NULL )"
                         )
        connect.myDatabase.commit()
        print("TABLE City created.")
    except Exception as e:
        print("TABLE City ERROR!!! ", e.args)

# create()
def insert(Name, Country, Population, Area):
    try:
        connect.mycursor.execute(f"INSERT INTO City (Name, Country, Population, Area) VALUES ('{Name}', '{Country}', '{Population}', '{Area}')")
        connect.myDatabase.commit()
        print("City inserted.")
    except:
        print("City ERROR!!!")


def update(Name, Country, Population, Area):
    try:
        connect.mycursor.execute(f"UPDATE City SET Population = '{Population}', Area = '{Area}' WHERE Name = '{Name}' AND Country = '{Country}'")
        connect.myDatabase.commit()
        print("City updated.")
    except:
        print("City ERROR!!!")


def delete(Name, Country):
    try:
        connect.mycursor.execute(f"DELETE FROM City WHERE Name = '{Name}' AND Country = '{Country}'")
        connect.myDatabase.commit()
        print("City deleted.")
    except:
        print("City ERROR!!!")
