#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : ap.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/4

import network


def run():
    ap = network.WLAN(network.AP_IF)
    ap.config(essid='esp32-web', authmode=network.AUTH_WPA_WPA2_PSK, password='esp32-web')
    ap.active(True)
    print('Network config:', ap.ifconfig())


if __name__ == '__main__':
    run()
