#!/usr/bin/python3
'''List all cities from the database hbtn_0e_4_usa'''
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
    cur.execute("SELECT cities.id AS city_id, cities.name AS city_name,\
            states.name AS state_name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    con.close()
