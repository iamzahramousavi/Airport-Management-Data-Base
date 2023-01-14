import connect
import streamlit as st

def pilotWithMostFights():
    """
    Finds the pilot with the most fights in the database.
    """
    query = "SELECT Pilot.name, COUNT(*) AS fights FROM Pilot, Flight WHERE Pilot.ID = Flight.Pilot GROUP BY Pilot.name ORDER BY fights DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)


def AirlinesWithMostFights():
    """
    Finds the airlines with the most fights in the database.
    """
    query = "SELECT Airline.name, COUNT(*) AS fights FROM Airline, Flight WHERE Airline.ID = Flight.Airline GROUP BY Airline.name ORDER BY fights DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)


def CitiesWithMostAirlines():
    """
    Finds the cities with the most airlines in the database.
    """
    query = "SELECT City.name, COUNT(*) AS airlines FROM City, Airline WHERE City.ID = Airline.City GROUP BY City.name ORDER BY airlines DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)

def CountOfFightsPerYear():
    """
    Finds the fights per year in the database.
    """
    query = "SELECT YEAR(Flight.date) AS year, COUNT(*) AS fights FROM Flight GROUP BY year ORDER BY year DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)


def CountOfFightsPerMonth():
    """
    Finds the fights per month in the database.
    """
    query = "SELECT MONTH(Flight.date) AS month, COUNT(*) AS fights FROM Flight GROUP BY month ORDER BY month DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)


def CountOfFightsPerDay():
    """
    Finds the fights per day in the database.
    """
    query = "SELECT DAY(Flight.date) AS day, COUNT(*) AS fights FROM Flight GROUP BY day ORDER BY day DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)


def CountOfPilotOfAirlines():
    """
    Finds the pilots per airlines in the database.
    """
    query = "SELECT Airline.name, COUNT(*) AS pilots FROM Airline, Pilot WHERE Airline.ID = Pilot.Airline GROUP BY Airline.name ORDER BY pilots DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)


def CountOfAirlinesPerCountry():
    """
    Finds the airlines per country in the database.
    """
    query = "SELECT Country.name, COUNT(*) AS airlines FROM Country, Airline WHERE Country.ID = Airline.Country GROUP BY Country.name ORDER BY airlines DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)



def CountOfFlightattendantsOfAirlines():
    """
    Finds the flightattendants per airlines in the database.
    """
    query = "SELECT Airline.name, COUNT(*) AS flightattendants FROM Airline, Flightattendant WHERE Airline.ID = Flightattendant.Airline GROUP BY Airline.name ORDER BY flightattendants DESC"
    connect.mycursor.execute(query)
    result = connect.mycursor.fetchall()
    st.info(result)