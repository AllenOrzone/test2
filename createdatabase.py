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
sql = '''create table user(
    username VARCHAR(30) not null primary key,
    password VARCHAR(30) not null);'''
cur.execute(sql)
print(cur.fetchall())
cur.close()
conn.close()