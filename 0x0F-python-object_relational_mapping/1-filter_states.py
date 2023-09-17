#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':

    con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    con.close()
