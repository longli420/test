# -*- coding:utf-8 -*-

# dict取第一个
d = {'1':98,'2':99,'3':90}

print(d['1'])


# dict key-vlue

x = {'1':90,'2':80,'3':100}
x['2'] = 10
print(x['2'])


# dict pop用法

v = {'1':20,'2':20,'3':40}

v.pop('1')

if v['2'] ==30:
    g = v['2'] +10
elif v['2'] !=30:
    g = v['2']-20
print(g)

