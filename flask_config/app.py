#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 10:34 
"""
# 实际工程应用中，通常结合【配置对象】【环境变量】两种方式
# 在配置对象中设置程序中所有用到的配置参数，并给予默认值保证程序正常启动运行，
# 然后再使用环境变量的方式来覆盖默认参数，保证最后的参数的正确性


from flask import Flask

from flask_config.config import Config

# 定义app
app = Flask(__name__)

# 从配置对象中加载配置
app.config.from_object(Config)

# 从配置文件加载
# app.config.from_pyfile('setting.py')

# 从系统环境变量加载配置
# 在pycharm中运行，记得点击【Edit Configurations】,然后在【Environment variables】中添加环境变量‘CONFIG_SETTING’
app.config.from_envvar('CONFIG_SETTING', silent=True)  # silent表示安静处理，即没有值也正常运行下去


# 定义接口
@app.route('/')
def hello():
    # 读取配置信息
    print('SECRET_KEY:{0}'.format(app.config.get('SECRET_KEY')))
    return 'hello'


# 启动
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
