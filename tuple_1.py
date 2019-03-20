# -*- coding: utf-8 -*-
#试题：输出Apple，Python Lisa
L = [
    ['apple','google','microsoft'],
    ['java','python','php'],
    ['adim','bart','lisa']
]
B = L[0]
C = L[1]
D = L[2]
print(B[0])
print(C[1])
print(D[2])

# 试题：在L的第2个列表增加一个list，输出
Y = [
    ['apple','google','microsoft'],
    ['java','python','php'],
    ['adim','bart','lisa']
]
F = ['ruby','javasrcipt']

G = Y[1]
G.append(F)

print(Y)

#试题：在第三个列表末尾删掉Lisa

H = [
    ['apple','google','microsoft'],
    ['java','python','php'],
    ['adim','bart','lisa']
]

J = H[2]

J.pop(2)
print(H)


# 试题：在第二个列表后增加一个列表

N = [
    ['apple','google','microsoft'],
    ['java','python','php'],
    ['adim','bart','lisa']
]

M = N[1]
S = ['ruby','javasrcipt']
M.insert(2,S)

print(M)