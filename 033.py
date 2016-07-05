#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import stdout

L = [1,2,3,4,5,6,7,8,9]
for c in L[:len(L)-1]:
    stdout.write(str(c))
    stdout.write(",")
print(str(L[-1]))

L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print s1
