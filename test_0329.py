# -*- coding:utf-8 -*-

# 获取本地时间
# import time
#
#
# time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print(time)
#
# import sys
# def Main():
#     sys.stdout.write('开始程序')
#     i = 1
#     print(i)
# if __name__ == '__main__':
#     Main()
# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
import math
# x = int(input('x:'))
# y = int(input('y:'))
# step = int(input('step:'))
# angle = int(input('angle:'))
#
# def move(x,y,step,angle):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx,ny
# print(move(x,y,step,angle))

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0的两个解。
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
def quadratic(a,b,c):
    if a==0 and b==0 and c!=0:
        return '此方程无解'
    elif a ==0 and b==0 and c==0:
        num1 = -b + math.sqrt((b*b-4*a*c)/2*a)
        num2 = -b - math.sqrt((b*b-4*a*c)/2*a)
        return num1,num2
    elif a!=0 and b!=0 and c!=0:
        num1 = -b + math.sqrt((b * b - 4 * a * c) / 2 * a)
        num2 = -b - math.sqrt((b * b - 4 * a * c) / 2 * a)
        return num1, num2