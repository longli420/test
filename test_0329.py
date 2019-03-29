# -*- coding:utf-8 -*-

# 获取本地时间
import time


time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time)