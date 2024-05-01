import mysql.connector
from mysql.connector import Error


def get_connect_mysql():
    try:
        # Establish connection to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            auth_plugin='caching_sha2_password',
            database="jaisriram",
            connect_timeout=10  # Adjust timeout as needed
        )

        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print("Error connecting to MySQL database:", e)


# Example usage
if __name__ == "__main__":
    connection = get_connect_mysql()
    # You can perform further operations with the connection here
