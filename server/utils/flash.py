#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : flash.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/6

import esp
import micropython

flash = esp.flash_size() / 1024 / 1024
memory = micropython.mem_info()

print(f"Total Flash Size:{flash}MB")
print(memory)

"""
stack: 736 out of 15360
GC: total: 56000, used: 1952, free: 54048, max new split: 57344
 No. of 1-blocks: 25, 2-blocks: 7, max blk sz: 18, max free sz: 3329
 
 栈空间:15kb
 堆空间:56kb
"""
