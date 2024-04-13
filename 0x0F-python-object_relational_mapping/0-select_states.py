#!/usr/bin/python3

"""This script lists all states from the database `hbtn_0e_0_usa`."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Extracting database credentials from command-line arguments
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

    # Executing SQL query to retrieve all states from the 'states' table
    db_cursor.execute(
        """
        SELECT * FROM states
        ORDER BY states.id;
        """
    )

    # Fetching all rows from the result set
    result_set = db_cursor.fetchall()

    # Displaying each row in the result set
    for state_row in result_set:
        print(state_row)

    # Closing the cursor and database connection
    db_cursor.close()
    connection.close()
