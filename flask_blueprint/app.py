#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/5 10:21 
"""
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello'


from flask_blueprint.admin import admin_blue
from flask_blueprint.user import user_blue

# 注册blueprint
app.register_blueprint(admin_blue)
app.register_blueprint(user_blue)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
