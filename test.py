# # -*- coding:utf-8 -*-
# # 删除某一元素或某一组
# s = ['a','b','c']
# h = ['a','b',s]
# h.pop(1)
# print(h)
#
# # 增加某一元素或某一组
# y = ['1','2','3']
# z = ['5','6']
# y.insert(2,z)
# print(y)
#
# # 末尾增加一个元素或组
# v = ['1','3', '5']
# m = ['7','8']
# v.append(m)
# print(v)
#
# # if判断
# # 登录接口
# username = '123'
# password = '123456'
# _username = input('输入账号：')
# _password = input('输入密码：')
# if _username == username and  _password == password:
#     print('登录成功')
# elif _username != username:
#     print('账号不正确')
# elif _password != password:
#     print('密码不正确')


# 回归练习


A = [ '1','2','3']

B = ['wang','zhang','li']

A.insert(1,B)
print(A)


C = ['1','2','3']
Y = ['w','j','q']
C.apped(Y)
print(C)