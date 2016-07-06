#!/usr/bin/python
# -*- coding: UTF-8 -*-
def reverse(s,l):
    t=[]
    for i in range(l):
        t.append(s[l-i-1])
    return t
s = [9,6,5,4,1]
print(reverse(s,len(s)))
