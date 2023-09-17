#!/usr/bin/python3
"""
in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    con.close()
