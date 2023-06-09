import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    database="user_test",
    charset="utf8",
    user="root",
    passwd="222666"
)
#检查账号是否有重复
cur = conn.cursor()
sql_1 = '''select username from user;'''
#插入数据库
# sql_2 = '''insert into user (username, password) values ('%s','%s');''' %(username, password)
cur.execute(sql_1)
result = cur.fetchall()

sql_2 = '''select * from user;'''
cur.execute(sql_2)
result_2 = cur.fetchall()
cur.close()
conn.close()

print(result, result_2)
print(type(result), type(result_2))
for i in result:
    print(i[0])