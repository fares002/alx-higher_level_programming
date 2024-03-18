#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
that start with the letter 'N'.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the query safely to avoid SQL injection
    query = "SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id` ASC"
    c.execute(query)

    # Fetch and print all the results
    for state in c.fetchall():
        print(state)

    # Close the cursor and the database connection
    c.close()
    db.close()
