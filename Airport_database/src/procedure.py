import connect



def load_procedures():
    """ Load procedures from files
    """

    # Load Delete procedure
    with open('src/procedures/SP_Delete.txt', 'r') as file:
        for line in file:
            connect.mycursor.execute(line)
            connect.myDatabase.commit()
    

    # Load Select procedure
    with open('src/procedures/SP_Select.txt', 'r') as file:
        for line in file:
            connect.mycursor.execute(line)
            connect.myDatabase.commit()

    # Load Update procedure
    with open('src/procedures/SP_Update.txt', 'r') as file:
        for line in file:
            connect.mycursor.execute(line)
            connect.myDatabase.commit()

    # Load Insert procedure
    with open('src/procedures/SP_Insert.txt', 'r') as file:
        for line in file:
            connect.mycursor.execute(line)
            connect.myDatabase.commit()
