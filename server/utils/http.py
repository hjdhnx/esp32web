#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : http.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/5

import requests
import urequests
# 不支持https请求

def get_ip():
    # r = urequests.get('http://httpbin.org/ip')
    r = requests.get('http://httpbin.org/ip')
    ret = r.json()
    print(ret)  # 打印返回的文本内容
    r.close()  # 关闭连接以释放资源
    return ret.get('origin')


def get_ip2():
    r = urequests.get("http://httpbin.org/get")
    ret = r.text
    print(ret)  # 打印返回的文本内容
    r.close()  # 关闭连接以释放资源
    return ret


if __name__ == '__main__':
    get_ip2()
