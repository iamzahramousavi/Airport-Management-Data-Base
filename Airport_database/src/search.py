import connect  
import streamlit as st
import pandas as pd
# import csv


def searchInDatabase():


    st.text("Now, let's search whatever you want")

    
    # st.write("Search by:")
    search_by = st.selectbox("", 
                            ["Select table to search", "Person", "Phone", "Passenger", "Pilot", 
                                "FlightAttendant", "Airline", "Airplane", "City", "Airport", 
                                "Flight", "Route", "Take"
                            ])
    # st.write("Search by: ", search_by)

    


    if search_by == "Select table to search":
        pass
    elif search_by == "Person":
        search_method = st.selectbox("",["Select Search Method","ID", "FirstName", "LastName", "Sex", "DateOfBirth"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word:", search_by)
    elif search_by == "Phone":
        search_method = st.selectbox("",["Select Search Method", "ID", "Type", "Number"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word:", search_by)
    elif search_by == "Passenger":
        search_method = st.selectbox("",["Select Search Method", "PassengerID", "FlyerStatus"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "Pilot":
        search_method = st.selectbox("",["Select Search Method", "PilotID", "YearsOfService"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "FlightAttendant":
        search_method = st.selectbox("",["Select Search Method", "FAID", "YearsOfService", "Rank"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "Airline":
        search_method = st.selectbox("",["Select Search Method", "carrier", "name"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "Airplane":
        search_method = st.selectbox("",["Select Search Method", "tailnum", "year", "manufacturer", "Model", "seats"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "City":
        search_method = st.selectbox("",["Select Search Method", "Name", "Country", "Population", "Area"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "Airport":
        search_method = st.selectbox("",["Select Search Method", "Code", "Name", "Lat", "Lon"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "Flight":
        search_method = st.selectbox("",["Select Search Method", "Date", "FlightNumber", "SchedArrTime", "SchedDepTime", "DepTime", "ArrTime", "Distance"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "Route":
        search_method = st.selectbox("",["Select Search Method", "Origin", "Dest"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    elif search_by == "Take":
        search_method = st.selectbox("",["Select Search Method", "Date", "FlightNumber", "SchedArrTime", "SchedDepTime", "PassengerID", "Type", "Class"])
        if search_method == "Select Search Method":
            pass
        elif search_method != None:
            search_key = st.text_input(f"Search in {search_by} with {search_method}, now type your key_word ", search_by)
    else:
        st.error("Please selelect a search method.")



    


    # if st.form_submit_button('Search'):
    # if st.button('search'):
    #     connect.mycursor.execute(f"SELECT * FROM {search_by} WHERE {search_method} = '{search_key}'")
    #     search_results = connect.mycursor.fetchall()
        
    #     st.table(search_results)


    if st.button('search'):




        # col1, col2 = st.columns([1, 1])

        # col1.subheader("Table Content")

        
        # search_by = "Select_" + search_by

        connect.mycursor.execute(f"SELECT * FROM {search_by} WHERE {search_method} = '{search_key}'")
        search_results = connect.mycursor.fetchall()
        connect.mycursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{search_by}'")
        search_results2 = connect.mycursor.fetchall()
        columns = []
        for item in search_results2:
            columns.append(item[0])
        data1 = pd.DataFrame(search_results, columns=(columns))
        # data1['actions'] = 'action' # -------------------------------------------------------------- add new column named 'action'
        # data1.assign(action = [st.button('delete')  ])
        # col1.table(data1)
        st.table(data1)


        # col2.subheader("Action Content")


        
        
        row_id = st.text_input("Enter row id to Delete or Edit: ")
        if st.button('delete'):
            pass
        if st.button('edit'):
            pass







        


        

        
    
       



        



        








# searchInDatabase()
