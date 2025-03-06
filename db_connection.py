import mysql.connector

# Establishing the connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # MySQL server host
            user="< >",       # add your MySQL username
            password="< >",  # add your MySQL password
            database="event_management"  # The database name
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    return connection  # In case there's no connection, return None
