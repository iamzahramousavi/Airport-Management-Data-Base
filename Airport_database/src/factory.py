import pymysql
# from tqdm import tqdm

myDatabase = pymysql.connect(
host="localhost",
user="root",
password="",
database="airport_database"
)

print("DATABASE CONNECT WELL.")
mycursor = myDatabase.cursor()

def data_factor():
    print("this is factory")
    try:
        counter = 1
        with open('src/data.txt') as f:
            print('3')
            for query in f:
                print(query)
                mycursor.execute(query)
                counter+=1
                myDatabase.commit()
    except:
        print("ERROR IN FACTORY")
        print("QUERY: ", query)
        print("COUNTER: ", counter)
        myDatabase.rollback()
    finally:
        myDatabase.close()
        print("Data loaded.")    
    