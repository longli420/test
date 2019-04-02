# -*- coding:utf-8 -*-
# x = 10
# def power(x):
#     return x*x
# print(power(x))
x=eval(input('请输入数字：'))
n =eval(input('请输入值：'))
# 调用
import math
def power(x,n):
    s = math.pow(x,n)
    return s
print(power(x,n))


#
# def enroll(name,gender):
#     print('name:', name)
#     print('gender:', gender)
# print(enroll('Sarah', 'F'))