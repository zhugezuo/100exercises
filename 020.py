#!/usr/bin/python
# -*- coding: UTF-8 -*-
s = -100.0
h = 100.0
n = input("n:")
for i in range(n):
    s += 2 * h
    h = h / 2
print s
