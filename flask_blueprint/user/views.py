#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：views.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/5 10:23 
"""
from flask_blueprint.user import user_blue


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
