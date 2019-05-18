#! /usr/bin/env python

import pyrebase
from flask import *

config = {
    "apiKey": "*************",
    "authDomain": "*************",
    "databaseURL": "*************",
    "projectId": "*************",
    "storageBucket": "*************",
    "messagingSenderId": "*************",
    "appId": "*************"
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()
# db.child("names").push({"name":"kota"})
# db.child("names").push({"name":"take"})

## app変数をFlaskで指定
app = Flask(__name__)

# ルートを指定、メソッドはGET、POST
@app.route('/', methods=['GET', 'POST'])

# basic関数を定義
def basic():
    # POSTでリクエストされたら
    if request.method == 'POST':
        # form['submit']のvalueが'add'であれば
        if request.form['submit'] == 'add':
            # formから値を取得
            name = request.form['name']
            # 値をfirebase上のtodoに書き込む
            db.child("todo").push(name)
            # firebaseから値を取得
            todo = db.child("todo").get()
            # toに値を代入
            to = todo.val()
            # index.htmlに 値toを返す
            return render_template('index.html', t=to.values())
        # form['submit']のvalueが'delete'であれば
        elif request.form['submit'] == 'delete':
            # firebaseのdbであるtodoを削除
            db.child("todo").remove()
            # 元のindex.htmlを返す
            return render_template('index.html',)
    # それ以外は、index.htmlを返す
    return render_template('index.html')

if __name__ == '__main__':
    #処理の実行
    app.run(debug=True)
