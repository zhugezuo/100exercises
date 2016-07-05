#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=[]
print("please enter ten numbers:")
for i in range(10):
    n.append(input())
for i in range(10):
    for j in range (i+1,10):
        if n[i]>n[j]:
            t=n[i]
            n[i]=n[j]
            n[j]=t
print n
