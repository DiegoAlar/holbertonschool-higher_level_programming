#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states\
    table of hbtn_0e_0_usa where name matches the argument. """

if __name__ == "__main__":

    import sys
    if (len(sys.argv) == 5):
        import MySQLdb

        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
        cur = db.cursor()
        cur.execute(
            "SELECT * FROM states\
             WHERE name LIKE '{}'\
             ORDER by id ASC".format(sys.argv[4]))
        rows = cur.fetchall()
        for col in rows:
            print(col)
        # Close all cursors
        cur.close()
        # Close all databases
        db.close()
