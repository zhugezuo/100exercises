#!/usr/bin/python
# -*- coding: UTF-8 -*-
x = [1,2,3,4,5,8,10,12,99,102]
l = len(x)
n=input("n:")
for i in range(l):
    if n < x[i]:
        x.append(x[l-1])
        for j in range(l-i):
            x[l-j]=x[l-j-1]
        x[i]=n
        break
print x
