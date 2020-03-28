#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists\
    all cities of that state, using the database hbtn_0e_4_usa """

if __name__ == "__main__":

    import sys
    if (len(sys.argv) == 5):
        import MySQLdb

        ans = ""
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
        cur = db.cursor()
        cur.execute(
            "SELECT cities.name\
             FROM `cities`\
             INNER JOIN `states`\
             ON cities.state_id=states.id\
             WHERE states.name LIKE \"{}\"".format(sys.argv[4]))
        rows = cur.fetchall()
        for col in rows:
            ans += col[0] + ", "
        print(ans[:-2])
        # Close all cursors
        cur.close()
        # Close all databases
        db.close()
