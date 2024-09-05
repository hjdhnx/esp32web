## web服务学习

### micropython
```python
help('modules')  # 查看所有安装的模块
```
### microdot
[参考文档](https://microdot.readthedocs.io/en/latest/index.html)

#### 设置静态目录
```python
from microdot import Microdot, Response, send_file
app = Microdot()

@app.route('/<path:path>')
async def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('dist/' + path, max_age=86400)
```