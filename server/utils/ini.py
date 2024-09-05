#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : ini.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/4

def write_ini_file(filename, config_dict):
    with open(filename, 'w') as f:
        for key, value in config_dict.items():
            f.write(f'{key} = {value}\n')


def read_ini_file(filename):
    config_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()  # 去除行尾的换行符和空格
            if line and not line.startswith('#'):  # 忽略空行和注释行（以 # 开头的行）
                key, value = line.split('=')  # 分割键和值
                config_dict[key.strip()] = value.strip()  # 将键和值添加到字典中，并去除前后的空格
    return config_dict
