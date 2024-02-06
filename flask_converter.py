#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask 
@File    ：flask_converter.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/4 11:17 
"""

from flask import Flask

app = Flask(__name__)


# flask原生的转换器
# int
# float
# string 任何不包含斜杠'/'的文本
# path 任何包含斜杠'/'的文本
@app.route('/hello/<int:id>')
def hello(id):
    return 'hello ' + str(id)


@app.route('/hello2/<string:id>')
def hello2(id):
    return 'hello2 ' + id


@app.route('/hello3/<path:id>')
def hello3(id):
    return 'hello3 ' + id


# 自定义转换器
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    """自定义转换器类"""

    def __init__(self, url_map, regex):
        # 调用父类的方法
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

# 将自定义转换器添加到flask应用中
app.url_map.converters['re'] = BaseConverter


# value的值必须符合re里面正则表达式的值
@app.route('/hello4/<re("123"):value>')
def hello4(value):
    print(value)
    return 'hello4'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
