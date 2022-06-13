import sys
import pymysql
import pandas as pd
import settings as st


""" MySQL Connector using pymysql"""
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

""" csv 파일로부터 dateframe 가져오기 """
df = pd.read_csv("C:/Users/user/Desktop/workspace/python/gcp-with-python/sql/아파트(매매)__실거래가_20050901_20060831.csv", encoding="utf-8-sig", error_bad_lines=False)

# print(df.head())
# print(df.info())
# print(df.describe())


df.to_sql(name="real_estate", con=conn, index=False)


# cur.execute("CREATE TABLE grade(name TEXT, phone TEXT, address TEXT)")
cur.execute("select * from real_estate")
# conn.commit()
conn.close()



