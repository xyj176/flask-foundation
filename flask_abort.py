#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_abort.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/4 16:08 
"""
# raise 主动抛出异常
# abort 在网页当中抛出异常

from flask import Flask, abort, request, make_response, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    abort(404)
    return '123'


@app.route('/index2', methods=['GET', 'POST'])
def index2():
    # get请求返回页面
    if request.method == 'GET':
        return render_template('index.html')
    # 点击【提交】触发post请求，如果用户名和密码不正确则抛出404
    if request.method == 'POST':
        name = request.form.get('账户')
        pw = request.form.get('密码')
        if name == 'zhangsan' and pw == '123':
            return 'login success'
        else:
            abort(404)  # 如果用户名和密码不正确的时候网页抛出404
            return None


# 自定义错误处理方法
# 如果index2接口触发了404错误，则会在这里进行处理
@app.errorhandler(404)
def handle_404_error(err):
    # return '发生404错误，错误信息是%s' % err
    return render_template('404.html')  # 返回404页面


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
