# -*- coding:utf-8 -*-


# set可以使数组去除
s = set([1,2,2,3,3])
print(s)

#  set 数组增加数组

d = set([3,4,5,6,6,7,6,6])
j = 1
m = 2
d.add(j)
d.add(m)
# 删除m
d.remove(m)
print(d)


# 两个set数组对比
l = set([1,2,3,3,3,4,5])
k = set([4,5,6,7,7,7])
print(l&k)
#两个set数组合并
f = set([1,2,3,3,3,4,5])
o = set([4,5,6,7,7,7])
print(f|o)

