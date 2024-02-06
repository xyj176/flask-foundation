#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_request.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/4 15:26 
"""
# request包含前端发送过来的所有请求数据
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    # 如果时get请求，则返回index.html页面
    if request.method == 'GET':
        return render_template('index.html')
    # 如果时post请求，则返回指定的字符串，并打印账户和密码
    # 点击页面中的【提交】按钮会触发post请求
    if request.method == 'POST':
        name = request.form.get('账户')
        password = request.form.get('密码')
        print(name, password)
        return 'this is post'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
