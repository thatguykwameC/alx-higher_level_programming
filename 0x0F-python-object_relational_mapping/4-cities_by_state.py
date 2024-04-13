#!/usr/bin/python3

"""This script displays all cities from the database `hbtn_0e_4_usa`
along with their corresponding state names."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Retrieving command-line arguments for database connection
    db_username, db_password, db_name = sys.argv[1:]

    # Establishing connection to the MySQL database
    connection = MySQLdb.connect(
        host="localhost",
        user=db_username,
        password=db_password,
        database=db_name,
        port=3306,
    )

    # Creating a cursor object to execute SQL queries
    db_cursor = connection.cursor()

    db_cursor.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
        """
    )

    # Fetching all rows from the result set
    result_set = db_cursor.fetchall()

    # Displaying each row in the result set
    for city_row in result_set:
        print(city_row)

    # Closing the cursor and database connection
    db_cursor.close()
    connection.close()
