#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import stdout
import math

n = int(input("请输入n："))
stdout.write(str(n))
stdout.write("=")
for i in range(2, n + 1):
    while (n != i):
        if (n % i == 0):
            stdout.write(str(i))
            stdout.write("*")
            n = n / i
        else:
            break
print '%d' % n
