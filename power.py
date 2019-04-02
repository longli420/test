# -*- coding:utf-8 -*-
# x = 10
# def power(x):
#     return x*x
# print(power(x))
# x=eval(input('请输入数字：'))
# n =eval(input('请输入值：'))
# # 调用
# import math
# def power(x,n):
#     s = math.pow(x,n)
#     return s
# print(power(x,n))
#

#
# def enroll(name,gender):
#     print('name:', name)
#     print('gender:', gender)
# print(enroll('Sarah', 'F'))

#
# def add_end(L=[]):
#     L.append('END')
#     return L
# print(add_end([1, 2, 3]))


#
# def add_end (l=[]):
#     l.append('end')
#     return l
# print(add_end([1,2,3]))
# list函数对比
l = set([1,2,3])
s = set([1,2,3,4])
def add_end (l,s):
    d = l|s
    return d
print(add_end(l,s))

