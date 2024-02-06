#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_static.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 10:11 
"""
from flask import Flask

# 默认static_url_path和static_folder，static_folder默认等于’static‘
# http://127.0.0.1:5050/static/a404.png
# app = Flask(__name__)

# 自定义static_url_path，flask3.x中，static_url_path默认等于static_folder参数
# http://127.0.0.1:5050/s/a404.png
# app = Flask(__name__, static_url_path='/s')

# 自定义static_folder，注意，如果自定义了static_folder，则无法再自定义static_url_path，static_url_path只能等于static_folder
# http://127.0.0.1:5050/static_custom/b404.png
app = Flask(__name__, static_folder='static_custom')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
