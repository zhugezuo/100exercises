#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True
count=0
for i in range(101,201):
    if isPrime(i):
        print i
        count+=1
print 'The total prime is %d' % count
