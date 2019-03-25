# -*- coding:utf-8 -*-

# 删除末尾元素
# x = ['a','b','c']
# x.pop(2)
# print(x)
# # 在末尾追加一个数组
# b = ['e','f','g']
# j = ['h','k']
# b.insert(1,j)
# print(b)
# # 在末尾增加一个数组
# n = ['1','2','3']
# m = ['5','6','7']
# n.append(m)
# print(n)
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
#
# name =input('请输入你的姓名：')
# H = eval(input('你的身高：'))
# W = eval(input('你的体重：'))
# BMI =W/(H*H)
# if BMI >=18.5:
#     print(name,'您的BMI指数为','%.2f'%BMI,'正常')
# elif BMI >=32:
#     print(name,'你的BMI指数为','%.2f'%BMI,'严重肥胖')
# elif BMI >=28:
#     print(name,'你的BMI指数为','%.2f'%BMI,'肥胖')
# elif BMI >=25:
#     print(name,'你的BMI指数为','%.2f'%BMI,'过重')
# else:
#     print(name,'你的BMI指数为','%.2f'%BMI,'过轻')


# 获取当前系统时间
import time
time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time)