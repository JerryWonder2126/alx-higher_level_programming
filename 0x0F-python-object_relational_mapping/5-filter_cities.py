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
    Fetches all cities that relates to a state in a database
    """
    USERNAME, PASSWORD, DBNAME, STATE_NAME = sys.argv[1:5]

    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD,
                           db=DBNAME, charset=CHARSET)
    with conn.cursor() as cur:

        cur.execute("""SELECT ct.id, st.name, ct.name FROM cities as ct
        INNER JOIN states as st ON ct.state_id = st.id AND st.name=%s ORDER BY
        id ASC""", (STATE_NAME,))
        query_rows = cur.fetchall()

        clean_result = [x[2] for x in query_rows]

        print(", ".join(clean_result))

    conn.close()


if __name__ == '__main__':
    run()
