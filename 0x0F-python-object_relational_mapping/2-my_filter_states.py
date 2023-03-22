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
    Fetches all states with name=STATE_NAME in database
    """
    USERNAME, PASSWORD, DBNAME, STATE_NAME = sys.argv[1:5]

    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD,
                           db=DBNAME, charset=CHARSET)

    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM states WHERE name=%s
         ORDER BY id ASC""", (STATE_NAME,))
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)
    conn.close()


if __name__ == '__main__':
    run()
