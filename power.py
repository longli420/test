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
# l = set([1,2,3])
# s = set([1,2,3,4])
# def add_end (l,s):
#     d = l|s
#     return d
# print(add_end(l,s))

# def add_end(l=None):
#     if l is None:
#         l =[]
#     l.append('end')
#     return l
# print(add_end())

# ---------------------------------------------------
#练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
import math
# x = [1,2,3]
# y = [5,6,7]
# def product(x, y):
#     x = x[0] + x[1] + x[2]
#     y = y[0] + y[1] + y[2]
#     return x * y
# print(product(x,y))

# x0 = eval(input('第一个列数字：'))
#
# x1 = eval(input('第二个列数字：'))
#
# x2 = eval(input('第三个列数字：'))
#
# y0 = eval(input('第一个数字：'))
#
# y1 = eval(input('第二个数字：'))
#
# y2 = eval(input('第三个数字：'))
#
# x = [x0,x1,x2]
# y = [y0,y1,y2]
# def product(x,y):
#     x = math.pow(x[0],2) + math.pow(x[1],2) + math.pow(x[2],2)
#     y = math.pow(y[0],2) + math.pow(y[1],2) + math.pow(y[2],2)
#     return math.pow(x*y,2)
# print(product(x,y))


# 多重数组算法
# 第一列
# import math
# list0 = eval(input('第一列数字：'))
# list1 = eval(input('第二列数字：'))
# list2 = eval(input('第三列数字：'))
#
# list = [list0,list1,list2]
#
# def Math(list):
#     x = math.pow(list0,2) * math.pow(list1,2) * math.pow(list2,2)
#     return x
# print(Math(list))

import math


x0 = eval(input('输入第一列数字:'))

x1 = eval(input('输入第二列数字:'))

x = [x0,x1]

def Math(x):
    x = math.pow(x0,2)*math.pow(x1,2)
    return x
print(Math(x))