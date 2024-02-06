#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_form.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/4 15:13 
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    # 返回templates下的index.html
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
