#!/usr/bin/python
# -*- coding: UTF-8 -*-
def isSXH(n):
    x=n/100
    y=(n/10)%10
    z=n%10
    if (x*x*x+y*y*y+z*z*z==n):
        return True
    else:
        return False


for i in range(100,1000):
    if isSXH(i):
        print i
