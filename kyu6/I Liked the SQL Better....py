import sqlite3
# Create a database /tmp/movies.db using SQLite3
# Create a table in it called "MOVIES"
# Insert data
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        sql ='''CREATE TABLE MOVIES(
           Name CHAR(200) NOT NULL,
           Year INT,
           Rating INT
        )
        '''
        cursor.execute(sql)
        ins = """INSERT INTO MOVIES 
        (Name,Year,Rating)
        VALUES 
        ("Rise of the Planet of the Apes",2011,77),
        ("Dawn of the Planet of the Apes",2014,91),
        ("Alien",1979,97),
        ("Aliens",1986,98),
        ("Mad Max",1979,95),
        ("Mad Max 2: The Road Warrior",1981,100)"""
        cursor.execute(ins)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
create_connection(r"/tmp/movies.db")
