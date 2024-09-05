#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : index.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/9/5

from microdot import Microdot, Response, send_file
from utils.file import file_exists
import time

Response.default_content_type = 'text/html'
app = Microdot()


@app.route('/')
async def index(request):
    with open('index.html', encoding='utf-8') as f:
        content = f.read()
    return Response(content, headers={'content-type': Response.default_content_type})


@app.before_request
async def start_timer(request):
    t1 = time.time()
    request.g.start_time = t1


@app.after_request
async def end_timer(request, response):
    t2 = time.time()
    duration = t2 - request.g.start_time
    print(f'Request took {duration:0.2f} seconds| time.time():{t2},request.g.start_time:{request.g.start_time}')


@app.route('/<path:path>')
async def static(request, path):
    if '..' in path or not file_exists(path):
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('dist/' + path, max_age=86400)
