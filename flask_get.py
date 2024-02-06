#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_get.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/4 10:07 
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return '/'


@app.route('/hello')
def hello2():
    return 'hello'


# http://127.0.0.1:5050/hello/xyj
@app.route('/hello/<name>')
def hello3(name):
    return 'hello ' + name


# http://127.0.0.1:5050/hello?name=xyj
@app.route('/hello4')
def hello4():
    name = request.args.get('name')
    return 'hello ' + name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
