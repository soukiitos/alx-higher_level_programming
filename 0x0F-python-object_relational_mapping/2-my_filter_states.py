#!/usr/bin/python3
"""
Take in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
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
    cur.execute("SELECT * FROM states WHERE\
            name LIKE BINARY '{}'".format(argv[4]))
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    con.close()
