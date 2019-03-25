# -*- coding:utf-8 -*-


import time
# 获取本地时间
# 格式化本地时间
# time.localtime(time.time())
time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time)