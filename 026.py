#!/usr/bin/python
# -*- coding: UTF-8 -*-
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)*n
n = input("n:")
print(fact(n))
