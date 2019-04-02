# -*- coding:utf-8 -*-

import time
# sum = 0
# n = 99
#
# while n > 0:
#     sum = sum + n
#     n = n - 2
#     print(sum)


# 如果x= 50的时候，中止循环
# for X in range(100):
#     if X == 50:
#         break
#     print(X)

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)
# n = 0
# while n<10:
#     n=n+1
#     if n % 2 == 0:
#         continue
#     print(n)



# 用户输入一个数，判断是否是偶数

# number = eval(input('请输入数字：'))
# if number % 2 !=0:
#     number = number +1
#     print(number)
# # else:
# #     number = number -1
# #     print(number)



# 练习

#用户输入一个数，判断是否为奇数


# number = eval(input("请输入一个数字："))
#
# # if number % 2 != 0:
# #     x = (number-1) /2
# #     print(x)
# # if x == (number-1) /2:
# #     print('end')
# if number % 2 == 0:
#     print(number)

#
# 利用time模块的格式化时间的方法来处理
# time.localtime(time.time())

# 获取当前时间进行判断
time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time)


