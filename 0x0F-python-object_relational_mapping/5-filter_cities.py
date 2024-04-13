#!/usr/bin/python3

"""This script lists all cities from the database `hbtn_0e_4_usa`
based on the provided state name, taken as an arguement."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Retrieving command-line arguments for database connection and state name
    db_username, db_password, db_name, state_name = sys.argv[1:]

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
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id;
        """,
        (state_name,),
    )

    # Fetching all rows from the result set
    result_set = db_cursor.fetchall()

    # Displaying the names of cities separated by commas
    print(", ".join(row[0] for row in result_set))

    # Closing the cursor and database connection
    db_cursor.close()
    connection.close()
