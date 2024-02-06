#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_redirect.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/4 15:42 
"""

from flask import Flask, redirect, url_for

app = Flask(__name__)


# 重定向网页
@app.route('/index')
def index():
    # 请求index接口回跳转到百度网页
    return redirect('https://www.baidu.com')


# 重定向接口
@app.route('/index2')
def index2():
    # 重定向到hello2方法，参数hello2是endpoint参数，app.route默认把视图函数(接口函数)的名称作为endpoint
    return redirect(url_for('hello2'))


@app.route('/hello')
def hello2():
    return 'this is hello fun'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
