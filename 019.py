#!/usr/bin/python
# -*- coding: UTF-8 -*-
for i in range(2, 1001):
    yinzi = []
    for j in range(1, i):
        if (i % j == 0):
            yinzi.append(j)
    if i == sum(yinzi):
        print (i)
        print (yinzi)
