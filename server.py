from flask import Flask, render_template, request, redirect, session
import pymysql

app = Flask(__name__)
app.secret_key = "affedasafafqwe"

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html", tip = '')
    else:
        #获取用户名密码
        username = request.form.get('account')
        password = request.form.get('password')
        print(username, password)

        if len(username) != 0 and len(password) != 0:
            #连接数据库
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
            cur.execute(sql_1)
            nameresult = cur.fetchall()
            for i in nameresult:
                if i[0] == username:
                    cur.close()
                    conn.close()
                    return render_template("register.html", tip = "傻篮子这用户名已经被人注册了")
            #插入数据库
            sql_2 = '''insert into user (username, password) values ('%s','%s');''' %(username, password)
            cur.execute(sql_2)
            conn.commit()
            cur.close()
            conn.close()
            return redirect('/')
        else:
            return render_template('register.html', tip = '草泥马傻逼东西不会打字是吧？')

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html', prompt = '')
    else:
        username = request.form.get('account')
        password = request.form.get('password')
        #连接数据库
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            database="user_test",
            charset="utf8",
            user="root",
            passwd="222666"
        )
        cur = conn.cursor()
        sql = '''select * from user;'''
        cur.execute(sql)
        result = cur.fetchall()
        #检查账号密码是否正确
        for i in result:
            if i[0] == username and i[1] == password:
                session['user_info']=username
                return redirect('/index')
        return render_template('login.html', prompt = '账号密码错误')

@app.route('/index')
def index():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/')
    return render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')