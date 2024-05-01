import mysql.connector
from mysql.connector import Error


def get_connect_mysql():
    try:
        # Establish connection to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password = 'Ycb@9603114404',
            database="data",

        )

        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print("Error connecting to MySQL database:", e)


