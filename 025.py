#!/usr/bin/python
# -*- coding: UTF-8 -*-
n = input("n:")
s = 0
for i in range(1,n+1):
    t = 1
    for j in range(1,i+1):
        t *= j
    s += t
print(s)
