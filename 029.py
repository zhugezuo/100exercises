#!/usr/bin/python
# -*- coding: UTF-8 -*-
n = int(raw_input("n:"))
l = len(str(n))
print ("%d是一个%d位数") % (n,l)
x = []
for i in range(l):
    x.append(n%10)
    n=n/10
print ("逆序的各位数字为：")
for c in x:
    print c
