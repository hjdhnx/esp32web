#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : file.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/5

import os


def file_exists(filename):
    try:
        # 尝试获取文件的状态信息
        os.stat(filename)
        return True  # 文件存在
    except OSError:
        return False  # 文件不存在
