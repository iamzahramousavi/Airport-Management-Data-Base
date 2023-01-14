import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Route ("
                         "Origin VARCHAR(3) NOT NULL,"
                         "Dest   VARCHAR(3) NOT NULL,"
                         "PRIMARY KEY(Origin,Dest),"
                         "foreign key (Origin) references Airport (Code) on delete cascade,"
                         "foreign key (Dest) references Airport (Code) on delete cascade )"
                         )
        connect.myDatabase.commit()
        print("TABLE Route created.")
    except Exception as e:
        print("TABLE Route ERROR!!! ", e.args)


def insert(Origin, Dest):
    try:
        connect.mycursor.execute(f"INSERT INTO Route (Origin, Dest) VALUES ('{Origin}', '{Dest}')")
        connect.myDatabase.commit()
        print("Route inserted.")
    except:
        print("Route ERROR!!!")


def update(Origin, Dest):
    try:
        connect.mycursor.execute(f"UPDATE Route SET Origin = '{Origin}', Dest = '{Dest}' WHERE Origin = '{Origin}' AND Dest = '{Dest}'")
        connect.myDatabase.commit()
        print("Route updated.")
    except:
        print("Route ERROR!!!")


def delete(Origin, Dest):
    try:
        connect.mycursor.execute(f"DELETE FROM Route WHERE Origin = '{Origin}' AND Dest = '{Dest}'")
        connect.myDatabase.commit()
        print("Route deleted.")
    except:
        print("Route ERROR!!!")


