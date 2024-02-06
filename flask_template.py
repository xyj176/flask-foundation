#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_template.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/5 9:38 
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        'name': '张三',
        'age': '18',
        'list': [1, 2, 3, 4]
    }
    # 把值传递给data参数，在前端页面渲染出来
    return render_template('index2.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
