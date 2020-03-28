#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":

    import sys
    if (len(sys.argv) == 4):
        import MySQLdb

        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER by id")
        rows = cur.fetchall()
        for col in rows:
            print(col)
        # Close all cursors
        cur.close()
        # Close all databases
        db.close()
