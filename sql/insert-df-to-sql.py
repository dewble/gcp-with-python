import sys
import pymysql
import pandas as pd
import settings as st


""" csv 파일로부터 dateframe 가져오기 """
# df = pd.read_csv("C:/Users/user/Desktop/workspace/python/gcp-with-python/sql/아파트(매매)__실거래가_20050901_20060831.csv", encoding="utf-8-sig", error_bad_lines=False)

# print(df.head())
# print(df.info())
# print(df.describe())


# df.to_sql(name="real_estate", con=conn, index=False)


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

""" create table """
# cur.execute("CREATE TABLE grade2(name TEXT, phone TEXT, address TEXT)")

"""delete"""
# DELETE FROM `real_estate`.`grade` WHERE  `name`='JM' AND `phone`='1531' AND `address`='Mapo' LIMIT 1;

"""insert"""
sql = """
INSERT INTO real_estate.grade2 (name, phone, address)VALUES (%s, %s, %s)
"""
for i in range(1, 10):
    try:
        cur.execute(sql, ("JM "+str(i), 1234+i, "MAPO"))
        conn.commit()
    except pymysql.Error as e:
        print(f"Error insert query: {e}")
        conn.close()


""" update """
# sql = """
# UPDATE real_estate.grade
# SET address = 'NAMGU'
# WHERE address = 'MAPO'
# """
# try:
#     cur.execute(sql)
#     conn.commit()
# except pymysql.Error as e:
#     print(f"Error update query: {e}")
#     conn.close()



