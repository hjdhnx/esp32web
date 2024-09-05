#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : wifi.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/5

from microdot import Microdot, Response
from utils.ini import write_ini_file
from utils.wifi import disconnect_wifi, get_wifi_info, scan_wifi
from utils.http import get_ip, get_ip2
import _thread
import server_wifi

Response.default_content_type = 'text/html'
app = Microdot()


@app.post('/save')
def save(req):
    wifiname = req.form.get('wifiname')
    wifipwd = req.form.get('wifipwd')
    print(wifiname, wifipwd)
    config = {
        'wifissid': wifiname,
        'wifipassword': wifipwd
    }
    write_ini_file('wificonfig.ini', config)
    print('esp32 starting server_wifi')
    _thread.start_new_thread(server_wifi.run, ())
    return 'wifi信息已配置'


@app.get('/disconnect')
def disconnect(req):
    print('esp32 wifi disconnect')
    ret = disconnect_wifi()
    return f'wifi连接已断开\n{ret}'


@app.get('/connect')
def connect(req):
    print('esp32 wifi connect')
    ret = server_wifi.run()
    return f'wifi已连接\n{ret}'


@app.get('/scan')
def scan(req):
    print('esp32 wifi scan')
    ret = scan_wifi()
    return ret


@app.get('/info')
def info(req):
    print('esp32 wifi info')
    ret = get_wifi_info()
    return f'wifi连接信息如下\n{ret}'


@app.get('/ip')
def ip(req):
    print('esp32 wifi ip')
    ret = get_ip()
    return f'公网ip:\n{ret}'


@app.get('/ip2')
def ip2(req):
    print('esp32 wifi ip2')
    ret = get_ip2()
    return f'公网ip:\n{ret}'
