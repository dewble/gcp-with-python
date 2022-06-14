import sys
import pymysql
import settings as st

""" MySQL Connector using pymysql"""
# connect
try:
    conn = pymysql.connect(
        user=st.USER,
        password=st.PASSWORD,
        host=st.HOST,
        port=st.PORT,
        database=st.DATABASE
    )
except pymysql.Error as e:
    print(f"Error connecting to mysql db: {e}")
    sys.exit(1)


# get cursor
cur = conn.cursor()

""" select - fetchall > List """
cur.execute("SELECT * FROM real_estate.grade2")
rows = cur.fetchall()
for row in rows:
    print(row)


# close
conn.close()