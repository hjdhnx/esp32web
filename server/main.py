#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : main.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/4


import server_wifi
import server_ap
import server_web
import _thread

if __name__ == '__main__':
    print('esp32 starting server_wifi')
    _thread.start_new_thread(server_wifi.run, ())
    print('esp32 starting server_ap')
    _thread.start_new_thread(server_ap.run, ())
    print('esp32 starting server_web')
    server_web.run()
