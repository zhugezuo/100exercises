#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = input("a:")
n = input("n:")
s = 0
for i in range(1, n + 1):
    s1 = 0
    for j in range(0, i):
        s1 += a * pow(10, j)
    s += s1
print(s)
