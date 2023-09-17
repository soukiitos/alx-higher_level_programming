#!/usr/bin/python3
"""
Takein the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.id, cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", [argv[4]])
    res = cur.fetchall()
    r = []
    for i in res:
        r.append(i[1])
    print(", ".join(r))
    cur.close()
    con.close()
