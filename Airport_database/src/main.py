import streamlit as st

from config import create_tables, drop_database
import factory
from search import searchInDatabase
from procedure import load_procedures
from insert import insert_to_database
from statistics import *


def main():
    st.set_page_config(layout="wide")
    st.title("Airport Management System")
    st.subheader("Welcome to Airport Management System")

    # st.write("This is a simple app to manage airport.")


    st.sidebar.text("First, let's create tables.")
    if st.sidebar.button("Create Tables"):
        create_tables()
        st.success("table created.")

        load_procedures()
        st.success("procedures created.")


    st.sidebar.text("Then, let's Load Data.")
    if st.sidebar.button("Load Data"):
        factory.data_factor()
        st.success("Data loaded.")

    st.sidebar.text("At the End, let's drop database.")
    if st.sidebar.button("Drop Database"):
        drop_database()
        st.success("database droped.")



    


    Search, Insert, Statistics = st.columns(3)

    with Search:
        st.header("Search Section")
        searchInDatabase()

    with Insert:
        st.header("Insert Section")
        st.text("Now, let's search whatever you want")
        insert_to_database()

    with Statistics:
        st.header("Statistics Section")
        st.text("Statistics Section")

        if st.checkbox("Pilot with most fights"):
            PilotWithMostFights()
        if st.checkbox("Airlines with most fights"):
            AirlinesWithMostFights()
        if st.checkbox("Cities with most airlines"):
            CitiesWithMostAirlines()
        if st.checkbox("Fights per year"):
            CountOfFightsPerYear()
        if st.checkbox("Fights per month"):
            CountOfFightsPerMonth()
        if st.checkbox("Fights per day"):
            CountOfFightsPerDay()
        if st.checkbox("Pilots per airlines"):
            CountOfPilotOfAirlines()
        if st.checkbox("Airlines per country"):
            CountOfAirlinesPerCountry()
        if st.checkbox("Flightattendants per airlines"):
            CountOfFlightattendantsOfAirlines()
        

    
    
    


    # if st.button('re-run'):
    #     st.experimental_rerun()


if __name__ == "__main__":
    main()
