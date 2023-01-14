import connect


def create():
    try:
        connect.mycursor.execute("CREATE TABLE Phone ("
                         "ID integer NOT NULL AUTO_INCREMENT,"
                         "Type varchar(20),"
                         "Number integer NOT NULL,"
                         "primary key (Number),"
                         "foreign key (ID) references Person (ID) on delete cascade )"
                         )
        connect.myDatabase.commit()
        print("TABLE Phone created.")
    except Exception as e:
        print("TABLE Phone ERROR!!! ", e.args)


def insert(ID, Type, Number):
    try:
        connect.mycursor.execute(f"INSERT INTO Phone (ID, Type, Number) VALUES ('{ID}', '{Type}', '{Number}')")
        connect.myDatabase.commit()
        print("Phone inserted.")
    except:
        print("Phone ERROR!!!")


def update(ID, Type, Number):
    try:
        connect.mycursor.execute(f"UPDATE Phone SET Type = '{Type}' WHERE ID = '{ID}' AND Number = '{Number}'")
        connect.myDatabase.commit()
        print("Phone updated.")
    except:
        print("Phone ERROR!!!")


def delete(ID, Number):
    try:
        connect.mycursor.execute(f"DELETE FROM Phone WHERE ID = '{ID}' AND Number = '{Number}'")
        connect.myDatabase.commit()
        print("Phone deleted.")
    except:
        print("Phone ERROR!!!")
