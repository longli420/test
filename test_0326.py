# -*- coding:utf-8 -*-
# -----------------------------
# append在末尾追加一个数组
d = ['1','2','3']
y = ['3','4','5']
d.append(y)
print(d)
# -----------------------------
# insert 指定在某一元素后插入数组
r = ['1','2','3']
t = ['3','4','5']
r.insert(1,t)
print(r)
# -----------------------------
# 删除数组某一元素
v = ['1','2','3']
v.pop(1)
print(v)

# -----------------------------
# dict
# 取第一个字典

n = {'1':20,'2':30,'3':40}
print(n['1'])

# 删除第一个字典
n.pop('1')
print(n)

# -----------------------------
# set
# 取重
we = set([1,2,3,3,4,4])
rt = set([4,5,6])
print(we&rt)

# 合并组

e = set([1,2,3,4,4])
y = set([5,6,7])
print(e|y)

# -----
ty = [1,2,3,4,4,5]
rl = set(ty)
print(rl)
# def
def my_base(x):
    if x>=0:
        return x
    else:
        return -x
# ----------------------------

# 获取本地时间
import time
# time.localtime(time.time())


time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

print(time)