#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : wifi.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/4

import network
import utime


def connect_wifi(ssid, password):
    """
    连接wifi
    :param ssid: wifi名称
    :param password: wifi密码
    :return:
    """
    wlan = network.WLAN(network.STA_IF)  # 创建WLAN对象，STA模式表示Station模式，即客户端模式
    wlan.active(True)  # 激活接口
    if not wlan.isconnected():  # 检查是否已经连接
        wlan.scan()
        print('connecting to network...')
        wlan.connect(ssid, password)  # 连接到指定的SSID和密码
        while not wlan.isconnected():  # 等待连接成功
            print('.', end='')
            utime.sleep(1)
    wlan_info = wlan.ifconfig()
    print('\nnetwork config:', wlan_info)  # 打印网络配置信息
    return wlan_info


def disconnect_wifi():
    """
    断开wifi连接
    :return:
    """
    wlan = network.WLAN(network.STA_IF)  # 创建WLAN对象，STA模式表示Station模式，即客户端模式
    wlan.active(True)  # 激活接口
    if wlan.isconnected():  # 检查是否已经连接
        print('已连接wifi:', wlan.ifconfig())  # 打印网络配置信息
        # 断开WiFi连接
        wlan.disconnect()
        while wlan.isconnected():  # 等待连接成功
            print('.', end='')
            utime.sleep(1)
    print('\n成功断开wifi连接')
    return wlan.ifconfig()


def get_wifi_info():
    """
    获取wifi连接信息
    :return:
    """
    wlan = network.WLAN(network.STA_IF)  # 创建WLAN对象，STA模式表示Station模式，即客户端模式
    wlan.active(True)
    return wlan.ifconfig()


def scan_wifi():
    """
    扫描wifi获取可用结果
    :return:
    """
    wlan = network.WLAN(network.STA_IF)  # 创建WLAN对象，STA模式表示Station模式，即客户端模式
    wlan.active(True)  # 激活接口
    networks = wlan.scan()  # 扫描可用的网络
    wifis = []
    for i, wifi in enumerate(networks):
        print(f"{i + 1}: {wifi[0]}, dBm: {wifi[3]}")
        wifis.append({
            'id': i + 1,
            'ssid': wifi[0],
            # 'bsid': ''.join(f'{b:02x}' for b in wifi[1]),
            'bsid': wifi[1],
            'channel': wifi[2],
            'dbm': wifi[3],
        })
    return wifis
