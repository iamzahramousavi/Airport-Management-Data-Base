import connect  
import streamlit as st

    


def insert_to_database():
    insert_method = st.selectbox("", 
                        ["Select table to INSERT","Person", "Phone", "Passenger", "Pilot", 
                            "FlightAttendant", "Airline", "Airplane", "City", "Airport", 
                            "Flight", "Route", "Take"
                        ])

    if insert_method == "Select table to INSERT":
        pass

    if insert_method :
        if(insert_method == "Select table to INSERT"):
            return 0
            
        # query = f"SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{insert_method}'"
        query = f"SELECT param_list FROM mysql.proc WHERE db='airport_database' AND name='IU_{insert_method}';"
        connect.mycursor.execute(query)
        res = connect.mycursor.fetchall()
        text = ''
        res = str(res)
        res = res.replace(" ", "")
        res = res.split("'")[1].split(",")
        
        dict = []
        for item in res:
            
            item = item.split('_')
            text += item[0] + ","

            if item[1] == "DATE":
                B = st.date_input('')
                A = str(B)
            else:
                A = st.text_input("", placeholder=f"{item[0]}")
                

            if item[1] == "INT":
                dict.append(int(A))
            else:
                dict.append(A)

        if st.button("Submit Insert"):
            curosor = connect.mycursor
            st.info(dict)
            curosor.callproc(f"IU_{insert_method}", dict)
            

            connect.myDatabase.commit()
