#!/usr/bin/python
# -*- coding: UTF-8 -*-
def reverse(s,l):
    t=[]
    for i in range(l):
        t.append(s[l-i-1])
    return t
s = raw_input("s:")
print(reverse(s,len(s)))
