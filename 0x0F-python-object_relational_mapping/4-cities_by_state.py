#!/usr/bin/python3

import sys
import MySQLdb

HOST = 'localhost'
PORT = 3306
USER = ''
PASSWORD = ''
DBNAME = ''
CHARSET = 'utf8'


def run():
    """
    Fetches all cities in database with their state name
    """
    USERNAME, PASSWORD, DBNAME = sys.argv[1:4]

    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD,
                           db=DBNAME, charset=CHARSET)
    with conn.cursor() as cur:

        cur.execute("""SELECT ct.id, st.name, ct.name FROM cities as ct
        INNER JOIN states as st ON st.id = ct.state_id ORDER BY id ASC""")
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    conn.close()


if __name__ == '__main__':
    run()
