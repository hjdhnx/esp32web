#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : server.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/4

from microdot import Microdot
from server.wifi import app as wifi_app
from server.index import app as index_app


def create_app():
    app = Microdot()
    app.mount(wifi_app, url_prefix='/wifi')
    app.mount(index_app, url_prefix='')
    return app


def run():
    app = create_app()
    app.run(debug=True, port=80)


if __name__ == '__main__':
    print('microdot server 已启动')
    run()
