#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

for i in range(10000):
    # 转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x * x == i + 100) and (y * y == i + 268):
        print i

x = map(lambda x: x * x, [y for y in range(101)])
for i in range(10000):
    if ((i + 100) in x) and ((i + 268) in x):
        print i
