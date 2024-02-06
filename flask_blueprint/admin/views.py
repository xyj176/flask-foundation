#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：views.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/5 10:28 
"""
from flask import Blueprint

# 第一个参数是Blueprint的名称，第二个参数是Blueprint所在的package的名称，通常都是__name__，第三个参数是路由前缀
admin_blue = Blueprint(name='admin', import_name=__name__, url_prefix='/admin')


@admin_blue.route('/alluser')
def alluser():
    return 'alluser'


@admin_blue.route('/deluser')
def deluser():
    return 'deluser'
