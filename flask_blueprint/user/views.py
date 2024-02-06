#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：views.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/5 10:23 
"""
from flask import Blueprint

# 第一个参数是Blueprint的名称，第二个参数是Blueprint所在的package的名称，通常都是__name__,第三个参数是路由前缀
user_blue = Blueprint(name='user', import_name=__name__, url_prefix='/user')


# 请求地址：ip+port+/user/register
@user_blue.route('/register')
def register():
    return 'register'


# 请求地址：ip+port+/user/login
@user_blue.route('login')
def login():
    return 'login'


# 请求地址：ip+port+/user/modify_pw
@user_blue.route('/modify_pw')
def modify_pw():
    return 'modify_pw'
