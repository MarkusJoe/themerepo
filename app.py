'''
Author: your name
Date: 2022-02-12 09:51:53
LastEditTime: 2022-02-12 09:55:30
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \undefinedc:\Users\Tapso\PycharmProjects\themerepo\app.py
'''
from flask import Flask


app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return {'code': 200,
            'msg': "Datadase index",
            'data': []}


@app.route('/assets')
def assets():
    return  app.send_static_file('theme.db')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    