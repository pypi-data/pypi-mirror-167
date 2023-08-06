## 使用线程模式打印log
 ```python
# 导入包
import vbigbang_thread_logging.core as logging2
   
# 初始化日志模块
logging2.init('test', "DEBUG")

# 打印日志
logging2.info('hello, world')
```

## 使用异步方式打印log
```python
# 导入包
from vbigbang_thread_logging.core import init_async_logger

# 初始化
logger = init_async_logger(module=f'async_test')

# 打印日志
logger.info('hello, world')
```

## 更新日志
```bash
     
2022-09-15: 首次上传

```
  
    

## 本地调试使用
1. 生成dist文件```python setup.py sdist```
2. 发布轮子```twine upload dist/*```
3. 参考```https://www.zywvvd.com/notes/coding/python/create-my-pip-package/create-my-pip-package/```