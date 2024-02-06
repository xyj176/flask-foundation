#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_hello.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 10:31 
"""
from flask import Flask

# 定义app
app = Flask(__name__)


# 定义接口
@app.route('/')
def hello():
    return 'hello'


# 启动
if __name__ == '__main__':
    # 运行flask提供的默认的调试服务器
    app.run(host='0.0.0.0', port=5050, debug=True)  # flask默认5000端口，host指定'0.0.0.0'可以跨机器访问接口，否则只能本机访问
