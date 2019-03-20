# -*- coding:utf-8 -*-

#
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

name = input('姓名：')
W = eval(input('您的体重（KG）:'))
H = eval(input('您的身高：(M):'))
L = H*H
BMI = W/L
if BMI > 32:
    print(name,'您的体重BMI指数','%.1f' %BMI,'严重肥胖')
elif BMI >= 28:
    print(name,'您的体重BMI指数', '%.1f' % BMI, '肥胖')
elif BMI >= 25:
    print(name,'您的体重BMI指数','%.1f'%BMI,'过重')
elif BMI >=18.5:
    print(name,'您的体重BMI指数','%.1f'%BMI,'正常')
else:
    print(name,'您的体重BMI指数','%.1f'%BMI,'过轻')