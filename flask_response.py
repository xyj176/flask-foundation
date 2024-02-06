#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_response.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/4 15:56 
"""
from flask import Flask, make_response, json, jsonify

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        'name': '张三'
    }
    # response = make_response(json.dumps(data, ensure_ascii=False))
    # response.mimetype = 'application/json'
    response = jsonify(data)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
