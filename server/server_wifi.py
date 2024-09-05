#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : server_wifi.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/5

from utils.wifi import connect_wifi
from utils.ini import read_ini_file


def run():
    config = read_ini_file('wificonfig.ini')
    # 检查是否已经连接
    print('connecting to network...')
    print((config['wifissid'], config['wifipassword']))
    # 连接到指定的SSID和密码
    try:
        return connect_wifi(config['wifissid'], config['wifipassword'])
    except Exception as e:
        print(f'连接wifi发生了错误:{e}')
