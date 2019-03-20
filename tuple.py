# -*- coding:utf-8 -*-

# 复习昨天学习
# 题目：在一个list里面先删除最后一个，再指定位置插入一个list，最后在末尾插入一个数组
# list元素
# classmates = ['mack','lucy','michel']
# classmates.pop(2)
# p = ['1','2']
# classmates.insert(1,p)
# l = [0,1]
# classmates.append(l)
# print(classmates)


# tuple
# t = ('a','b',[1,2])
# t[2][0] = 3
# t[2][1] = 4
# print(t)
# t = (1,2)
# print(t)

# 定义一个空的tuple，可以写成()
# t = ()
# print(t)

# 练习

l = [
    ['apple','google','microsoft'],
    ['java','python','ruby','php'],
    ['admin','user','lisa']
]
# 打印Apple
t = l[0][0]
print(t)
# 打印Python
h = l[1][1]
print(h)
# 打印Lisa
j = l[2][2]
print(j)
print(t,h,j)