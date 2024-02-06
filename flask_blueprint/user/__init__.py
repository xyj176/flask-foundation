#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/5 10:23 
"""

from flask import Blueprint

# 定义蓝图
# 第一个参数是Blueprint的名称，第二个参数是Blueprint所在的package的名称，通常都是__name__,第三个参数是路由前缀
user_blue = Blueprint(name='user', import_name=__name__, url_prefix='/user')

# 引入view，让view里面的接口生效（一定要放置在最后）
from . import views
