#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : path.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/6

def path_join(*parts):
    # 拼接路径并按 / 分割
    path = '/'.join(part.strip('/') for part in parts)

    # 处理 '.' 和 '..'
    components = []
    for part in path.split('/'):
        if part == '' or part == '.':
            # 忽略空字符串或当前目录
            continue
        elif part == '..':
            # 如果有上级目录，则回退到上一级
            if components:
                components.pop()
        else:
            # 否则添加到路径中
            components.append(part)

    # 返回处理后的路径
    return '/' + '/'.join(components)


def path_dirname(path):
    return '/'.join(path.strip('/').split('/')[:-1])


def path_abspath(path):
    # 如果假设路径是绝对路径，直接返回
    if not path.startswith('/'):
        return '/' + path
    return path
