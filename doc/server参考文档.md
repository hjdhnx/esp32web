## 项目从零搭建

### 参考教程

- [基于esp32 C3的micropython开热点web配置无线网络保姆级教程](https://blog.csdn.net/qq_33413128/article/details/137437042)
- [小白学习Esp32_micropython编程笔记 ——网络通讯基础（1）](https://zhuanlan.zhihu.com/p/691938955?utm_id=0)
- [microdot官方手册](https://microdot.readthedocs.io/en/latest/index.html)

## web服务学习

### micropython

```python
help('modules')  # 查看所有安装的模块
import mip # 导入类似的pip工具
mip.install("microdot") # 安装库
```

mip可安装的应用仓库 [micropython-lib](https://github.com/micropython/micropython-lib)  
thonny-micropython设备-储存空间可以看到剩余flash内存  
比如我的2mb的设备显示 总空间320kb
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