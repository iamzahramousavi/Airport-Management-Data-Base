import pymysql
import streamlit as st


myDatabase = pymysql.connect(
host="localhost",
user="root",
password="",
)

print("DATABASE CONNECT WELL.")
mycursor = myDatabase.cursor()

def create_database():
    try:
        mycursor.execute(
            "CREATE DATABASE airport_database"
        )
        myDatabase.commit()
        print("DATABASE Created.")

    except:
        print("DATABASE Creation ERROR!!!")
        myDatabase.rollback()

    # finally:
    #     if myDatabase:
    #         myDatabase.close()



st.title("Airport Management System")
st.subheader("Create Database")
if st.button("Create Database"):
    create_database()
    st.success("Database Created.")
