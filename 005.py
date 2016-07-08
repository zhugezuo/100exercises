#!/usr/bin/python
# -*- coding: UTF-8 -*-
x = input("x:")
y = input("y:")
z = input("z:")


def sort(i, j):
    if i > j:
        t = i
        i = j
        j = t
    return i, j


x, y = sort(x, y)
x, z = sort(x, z)
y, z = sort(y, z)
print x, y, z

l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l
