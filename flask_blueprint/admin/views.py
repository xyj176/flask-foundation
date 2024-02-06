#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：views.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/5 10:28 
"""
from flask_blueprint.admin import admin_blue


@admin_blue.route('/alluser')
def alluser():
    return 'alluser'


@admin_blue.route('/deluser')
def deluser():
    return 'deluser'
