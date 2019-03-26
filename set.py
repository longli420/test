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


# 两个set数组对比取重
l = set([1,2,3,3,3,4,5])
k = set([4,5,6,7,7,7])
print(l&k)
#两个set数组合并
f = set([1,2,3,3,3,4,5])
o = set([4,5,6,7,7,7])
print(f|o)

# test 两个数组去重后合并，并增加一个元素
if f|o =={1,2,3,4,5,6,7}:
    a = f|o
    a.add(8)
print(a)

# test 两数组对比取重之后再追加一个元素，删除取重的某一元素
w = set([1,2,3,4,4,4,5,6,7])
q = set([1,2,3,4,5])
u = {1,2,3,4,5}
if w&q ==u:
    g = w&q
    g.add(6)
    g.remove(1)
print(g)
# replace 改变不了变量 只会把变量赋值
ml = 'abc'
lm = ml.replace('a','A')
print(lm)


