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
    Fetches all states in database
    """
    USERNAME, PASSWORD, DBNAME = sys.argv[1:4]

    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD,
                           db=DBNAME, charset=CHARSET)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    run()
