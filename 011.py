#!/usr/bin/python
# -*- coding: UTF-8 -*-
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


n = input("n:")
print fib(n)
