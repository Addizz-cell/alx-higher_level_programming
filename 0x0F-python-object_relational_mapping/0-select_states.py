
#!/usr/bin/python3
"""  lists all states from the database """
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to get all states
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all rows using fetchall() method
    states = cursor.fetchall()

    # Print states
    for state in states:
        print(state)

    # Disconnect from server
    cursor.close()
    db.close()
