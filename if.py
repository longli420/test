# -*- coding:utf-8 -*-
import numpy
# if
# age = 20
#
# if age >=18:
#     print('your age is',age)

# if&else

# age = 3
# if age >= 18:
#     print('your age is',age)
# else:
#     print('your age is',age)


# elif
# l =20
# age = int(input('猜下年龄：'))
# if age > l:
#     print('大了')
# elif age == l / 2:
#     print('你猜对了一半')
# elif age < l:
#     print('小了')
# elif age == l:
#     print('你猜对了')
# else:
#     print('game over')


# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

s = 1.75
h = s*s
n = 80.5

k = 18.5
j = 25
l = 28
c = 32
BMI = n/h
nuber = int(input('猜下数字：'))

if nuber < k:
    print('过轻')
elif k < nuber < j:
    print('正常')
elif j < nuber < l:
    print('过重')
elif l < nuber < c:
    print('肥胖')
elif nuber > c:
    print('严重肥胖')
