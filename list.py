import sys

# print('I\'m ok')
# print("I \n 'm ok")
# print('\\\t\\')
# print(r'\\\t\\')
# print('''line1
# line2
# line3''')
#
#
# print(r'''hello,\n
# world''')
#
# # 变量与字符串
#
# a=1
# b="123"
#
# print(a)
# print(b)
#
# -*-coding:utf-8 -*-
# test002
# n= 123
# f=456.789
# s1 = 'hello,world'
# s2 = 'hello,\'Admin\''
# s3 = r'hello,"bart"'
# s4 = r'''hello,
# lisa!'''
#
# print(s4)
# test003
# s1 = 72
# s2 = 85
# r = (85-72)/100*100
# print (r)
#
#
#
# list列表
# classmates = ['mack','may','bob']
# print(classmates)
#
# list列表个数
# classmates = len(['mack','may','bob'])
# print(classmates)
#
# 末尾追加元素
# classmates = ['mack','rose','lucy']
#
# classmates.append('mick')
#
# print(classmates)
#
# 元素插入到指定的位置
#
# classmates = ['mack','may','lucy']
# classmates.insert(1,'jack')
# one = len(classmates)
#
# print(one)
#
# 删除指定区域的元素
# classmates = ['mack','may','lucy']
#
# classmates.pop(1)
#
# print(classmates)
#
# 某元素替换成别的元素，可以赋值给对应的索引位置
# classmates = ['mack','may','lucy']
# classmates[1] = 'wang'
# print(classmates)
#
# list 也可是一个另一个list
# classmates = ['mack',['mack','lucy'],'may']
# s = len(classmates)
# print(s)
#
# 为list追加一个list
# classmates = ['mack',['mack','lucy'],'lucy']
#
# s = classmates.insert(1,['lcy','none'] )
#
# h = classmates
#
# print(h)

# 为list索引为1追加一个list，删除最后一个

classmates  = ['mack','lucy','none1']
p = ['mack','lucy']
s = classmates.insert(1,p)
# print(h)
classmates.pop(3)

print(classmates)