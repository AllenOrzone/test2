import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    database="user_test",
    charset="utf8",
    user="root",
    passwd="222666"
)

cur = conn.cursor()
sql = '''insert into user (username, password) values ('nidie','nidie');'''
cur.execute(sql)
conn.commit()
cur.close()
conn.close()