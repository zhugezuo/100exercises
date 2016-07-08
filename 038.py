#!/usr/bin/python
# -*- coding: UTF-8 -*-
n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum = 0.0
print ("Please enter 3 * 3 numbers:")
for i in range(3):
    for j in range(3):
        n[i][j] = (input())
for i in range(3):
    sum += n[i][i]
print sum
