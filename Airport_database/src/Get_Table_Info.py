import connect

connect.mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='airport_database'")

table_name = connect.mycursor.fetchall()
table_name = [item[0].replace(",", '') for item in table_name]

text = ''
for i in table_name:
    query = f"SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{i}'"
    connect.mycursor.execute(query)
    res = connect.mycursor.fetchall()
    with open("Table_Info.txt", "w") as f:
        text += i + "\n"
        for item in res:
            # print(i, ", " ,item)
            text += item[0] + "," + item[1]
            if(type(item[2]) != type(None)):
                text += "," + str(item[2]) + "\n"
            else:
                text += "\n"
        text += "#\n"
        # f.write(text)

print(text)

print("done.")